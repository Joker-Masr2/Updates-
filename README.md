# CreatingTool Updater

**Current Version:** 1.0  
**Repository:** [Joker-Masr2/CreatingTool](https://github.com/Joker-Masr2/CreatingTool)

---

## Overview

This is an **updater module** for the CreatingTool project.  
It can be integrated into the main tool to automatically check for updates on GitHub and update the local files.

> ⚠️ This module **does not run standalone**. It must be imported and called from the main tool.

---

## 🔄 Auto Update

This tool supports **automatic self-updating** from GitHub. Here's how it works:

1. The tool uses the **GitHub API** to check the latest **release** of the repository.
2. Each new release must have a **Tag** (e.g., `v1.0`, `v1.1`).
3. The code compares this tag with the current version (`__version__`) in the script.
4. If the latest version is different from the current version:
   - The tool downloads the ZIP file of the latest release.
   - It extracts the files.
   - It replaces the old files with the new ones.
   - Finally, it **restarts itself automatically** so the update takes effect.

### ⚠️ Important Notes
- Without a **Tag**, the tool cannot detect the new release, so no update will be downloaded.
- Make sure to update the `__version__` in the code for every important release.

### 💡 Tip
Always create a **Tag** on GitHub for every new release to ensure the auto-update works smoothly.---

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
