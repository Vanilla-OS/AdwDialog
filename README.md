<div align="center">
  <img src="adwdialog-logo.png" height="120">
  <h1 align="center">AdwDialog</h1>
  <p align="center">Display GTK4/libadwaita dialogs from terminal and scripts.</p>
</div>

<br/>

## Help

```
Usage:
  adwdialog [OPTION…]

Help Options:
  -h, --help                 Show help options
  --help-all                 Show all help options
  --help-gapplication        Show GApplication options

Application Options:
  -t, --title                The dialog title
  -d, --description          The dialog description
  -i, --icon                 The dialog icon (optional)
  -y, --type                 The dialog type
```

## Build

```bash
meson mesonbuild
cd mesonbuild
ninja install
```
