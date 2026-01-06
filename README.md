# CreatingTool Updater

**Current Version:** 1.0  
**Repository:** [Joker-Masr2/CreatingTool](https://github.com/Joker-Masr2/CreatingTool)

---

## Overview

This is an **updater module** for the CreatingTool project.  
It can be integrated into the main tool to automatically check for updates on GitHub and update the local files.

> ⚠️ This module **does not run standalone**. It must be imported and called from the main tool.

---

## Features

- Check for latest release on GitHub.
- Download and install updates automatically.
- Replace existing files safely.
- Restart the main tool after updating.
- Handles update errors gracefully.

---

## Integration

1. Copy `updater.py` to your tool's directory.
2. Import and call the updater in your main code:
   ```python
   from updater import fix_me

## Run updater before starting the main tool
`fix_me()`
The updater will check for the latest version.
If your version is outdated, it will download the update, replace files, and restart the tool.
If your version is up to date, it will do nothing.

## Requirements
Python 3.8+
requests
packaging
1. Install dependencies using:
   ```bash
   pip install -r requirements.txt

## Notes
Make sure the updater runs inside the tool directory.
Internet connection is required.
Works on Windows, Linux, and macOS.
Backup your work if necessary—files will be replaced.

## License
MIT License — open for personal use and modification.
