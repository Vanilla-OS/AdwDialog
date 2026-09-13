<div align="center">
  <img src="adwdialog-logo.png" height="120">
  <h1 align="center">AdwDialog</h1>
  <p align="center">Display GTK4/libadwaita dialogs from terminal and scripts.</p>
</div>

<br/>

## Help

```sh
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
meson setup build
ninja -C build install
```

## Use of Generative AI

Maintainers may use generative AI tools as assistants while working on AdwDialog. Non-trivial assisted commits disclose the tool, model, and scope of the work.

AI tools may assist with code comments, documentation, repetitive code, and issue triage. Maintainers make project decisions and review every assisted change before it is merged.

Use these trailers for non-trivial assisted commits:

```plain
Assisted-by: <tool>:<model-version>
AI-Scope: <what the tool generated and the prompt or a short prompt summary>
```

Single-line completions, renames, and formatting changes do not need trailers.

Coding agents must also follow [AGENTS.md](AGENTS.md) before changing files,
creating commits, or opening pull requests.
