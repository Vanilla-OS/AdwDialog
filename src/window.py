# window.py
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
from gi.repository import Adw
from gi.repository import Gtk

@Gtk.Template(resource_path='/org/vanillaos/AdwDialog/window.ui')
class AdwdialogWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'AdwdialogWindow'

    status = Gtk.Template.Child()
    box_btns = Gtk.Template.Child()

    def __init__(self, title, description, icon, dtype, **kwargs):
        super().__init__(**kwargs)

        self.set_title("")
        self.status.set_title(title)
        self.status.set_description(description)

        if icon:
            self.status.set_icon_name(icon)
        elif dtype == "info":
            self.status.set_icon_name("dialog-information-symbolic")
        elif dtype == "warning":
            self.status.set_icon_name("dialog-warning-symbolic")
        elif dtype == "error":
            self.status.set_icon_name("dialog-error-symbolic")
        elif dtype == "question":
            self.status.set_icon_name("dialog-question-symbolic")

        self.__build_buttons(dtype)

    def __build_buttons(self, dtype):
        if dtype == "info":
            self.__add_button(_("Dismiss"), 0, True)
        elif dtype == "warning":
            self.__add_button(_("Dismiss"), 0, True)
        elif dtype == "error":
            self.__add_button(_("Dismiss"), 0, True)
        elif dtype == "question":
            self.__add_button(_("Yes"), 1, True)
            self.__add_button(_("No"), 0)

    def __add_button(self, label, action, suggested=False):
        btn = Gtk.Button(label=label)
        btn.connect("clicked", self.__on_button_clicked, action)
        btn.add_css_class("pill")

        if suggested:
            btn.add_css_class("suggested-action")

        self.box_btns.append(btn)

    def __on_button_clicked(self, widget, action):
        sys.exit(action)
