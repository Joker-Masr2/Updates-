import requests
import zipfile
import os
import shutil
import sys
from packaging import version
#https://github.com/Joker-Masr2/Updates-/upload/main
__version__ = "1.0.0"
REPO = "Joker-Masr2/Updates-"  # غيرها

# -----------------------------
# Check for updates
# -----------------------------
def check_update():
    url = f"https://api.github.com/repos/{REPO}/releases/latest"
    try:
        r = requests.get(url, timeout=5)
        r.raise_for_status()

        latest = r.json()["tag_name"].lstrip("v")

        if version.parse(latest) > version.parse(__version__):
            return latest
        return None

    except Exception as e:
        print(f"[!] Update check failed: {e}")
        return None


# -----------------------------
# Download & install update
# -----------------------------
def install_update(latest_version):
    zip_url = f"https://github.com/{REPO}/archive/refs/tags/v{latest_version}.zip"
    zip_name = "update.zip"
    temp_dir = "update_temp"

    print("[*] Downloading update...")

    r = requests.get(zip_url, stream=True)
    with open(zip_name, "wb") as f:
        for chunk in r.iter_content(1024):
            f.write(chunk)

    print("[*] Extracting update...")

    with zipfile.ZipFile(zip_name, "r") as zip_ref:
        zip_ref.extractall(temp_dir)

    extracted_folder = os.listdir(temp_dir)[0]
    source_path = os.path.join(temp_dir, extracted_folder)

    print("[*] Installing update...")

    for item in os.listdir(source_path):
        src = os.path.join(source_path, item)
        dst = item

        if os.path.isdir(src):
            shutil.copytree(src, dst, dirs_exist_ok=True)
        else:
            shutil.copy2(src, dst)

    shutil.rmtree(temp_dir)
    os.remove(zip_name)

    print("[✓] Update installed successfully")
    restart_program()


# -----------------------------
# Restart tool
# -----------------------------
def restart_program():
    print("[*] Restarting tool...")
    python = sys.executable
    os.execv(python, [python] + sys.argv)


# -----------------------------
# Auto update logic
# -----------------------------
def auto_update():
    latest = check_update()

    if latest:
        print(f"[+] New version available: {latest}")
        choice = input("Do you want to update now? (y/N): ")

        if choice.lower() == "y":
            install_update(latest)
    else:
        print("[✓] You are using the latest version")


# -----------------------------
# Tool main logic
# -----------------------------
def main():
    auto_update()

    print("\n=== TOOL STARTED ===")
    print(f"Running version {__version__}")
    # هنا شغلك الحقيقي
    input("Press Enter to exit...")


if __name__ == "__main__":
    main()