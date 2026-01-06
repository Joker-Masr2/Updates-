import requests
import zipfile
import os
import shutil
import sys
from packaging import version
##update
__version__ = "1.0"
REPO = "Joker-Masr2/CreatingTool" #Change it

def fix_me():
    try:
        api = f"https://api.github.com/repos/{REPO}/releases/latest"
        data = requests.get(api, timeout=5).json()
        latest = data["tag_name"].lstrip("v")
		
        if version.parse(latest) == version.parse(__version__):
            return

        print(f"[{g}+{w}]{g} Update found:{p} {latest}{l}")
        time.sleep(.3)
        print(f"[{y}+{w}] {y}Installing...")
        time.sleep(2)

        zip_url = f"https://github.com/{REPO}/archive/refs/tags/v{latest}.zip"
        r = requests.get(zip_url, stream=True)

        with open("update.zip", "wb") as f:
            for c in r.iter_content(1024):
                f.write(c)

        with zipfile.ZipFile("update.zip") as z:
            z.extractall("upd")

        folder = os.listdir("upd")[0]
        for i in os.listdir(f"upd/{folder}"):
            s = f"upd/{folder}/{i}"
            if os.path.isdir(s):
                shutil.copytree(s, i, dirs_exist_ok=True)
            else:
                shutil.copy2(s, i)

        shutil.rmtree("upd")
        os.remove("update.zip")

        restart()

    except Exception as e:
        print(f"[!] Update error: {e}")

def restart():
    os.execv(sys.executable, [sys.executable] + sys.argv)

# run fix_me()
