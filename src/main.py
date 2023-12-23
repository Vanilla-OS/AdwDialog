# main.py
#
# Copyright 2022 Mirko Brombin <send@mirko.pm>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

import sys
import gi

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

from gi.repository import Gtk, Gio, GLib, Adw
from .window import AdwdialogWindow


class AdwdialogApplication(Adw.Application):
    """The main application singleton class."""

    title: str = None
    description: str = None
    icon: str = None
    dtype: str = None
    default_label: str = None
    suggested_label: str = None

    def __init__(self):
        super().__init__(application_id='org.vanillaos.AdwDialog',
                         flags=Gio.ApplicationFlags.HANDLES_COMMAND_LINE)
        self.create_action('quit', self.quit, ['<primary>q'])
        self.__register_arguments()

    def __register_arguments(self):
        """Register the command line arguments."""
        self.add_main_option('title', ord('t'), GLib.OptionFlags.NONE,
                             GLib.OptionArg.STRING, 'The dialog title', None)
        self.add_main_option('description', ord('d'), GLib.OptionFlags.NONE,
                             GLib.OptionArg.STRING, 'The dialog description', None)
        self.add_main_option('icon', ord('i'), GLib.OptionFlags.NONE,
                             GLib.OptionArg.STRING, 'The dialog icon', None)
        self.add_main_option('type', ord('y'), GLib.OptionFlags.NONE,
                             GLib.OptionArg.STRING, 'The dialog type', None)
        self.add_main_option('default_label', ord('d'), GLib.OptionFlags.NONE,
                             GLib.OptionArg.STRING, 'The dialog default label', None)
        self.add_main_option('suggested_label', ord('s'), GLib.OptionFlags.NONE,
                             GLib.OptionArg.STRING, 'The dialog suggested label', None)

    def do_command_line(self, command_line):
        """Handle command line arguments."""
        options = command_line.get_options_dict()
        if options.contains('title'):
            self.title = options.lookup_value('title').get_string()
        if options.contains('description'):
            self.description = options.lookup_value('description').get_string()
        if options.contains('icon'):
            self.icon = options.lookup_value('icon').get_string()
        if options.contains('type'):
            self.dtype = options.lookup_value('type').get_string()
        if options.contains('default_label'):
            self.default_label = options.lookup_value('default_label').get_string()
        if options.contains('suggested_label'):
            self.suggested_label = options.lookup_value('suggested_label').get_string()
        self.activate()
        return 0

    def do_activate(self):
        """Called when the application is activated.

        We raise the application's main window, creating it if
        necessary.
        """
        if None in (self.title, self.description, self.dtype):
            print('Missing essential arguments: --title --description --type')
            sys.exit(1)

        win = self.props.active_window
        if not win:
            win = AdwdialogWindow(application=self, title=self.title,
                                  description=self.description, icon=self.icon,
                                  dtype=self.dtype, default_label=self.default_label,
                                  suggested_label=self.suggested_label)
        win.present()

    def create_action(self, name, callback, shortcuts=None):
        """Add an application action.

        Args:
            name: the name of the action
            callback: the function to be called when the action is
              activated
            shortcuts: an optional list of accelerators
        """
        action = Gio.SimpleAction.new(name, None)
        action.connect("activate", callback)
        self.add_action(action)
        if shortcuts:
            self.set_accels_for_action(f"app.{name}", shortcuts)


def main(version):
    """The application's entry point."""
    app = AdwdialogApplication()
    return app.run(sys.argv)
