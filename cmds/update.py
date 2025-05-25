import requests
import zipfile
import io
import os
import shutil
import sys

def run(args):
    zip_url = "https://github.com/bowser-2077/HessOS/archive/refs/heads/main.zip"

    print("Downloading latest HessOS update...")
    try:
        r = requests.get(zip_url)
        r.raise_for_status()
    except Exception as e:
        print(f"Download failed: {e}")
        return

    print("Download complete. Extracting...")
    with zipfile.ZipFile(io.BytesIO(r.content)) as zip_ref:
        tmp_dir = "hessos_update_tmp"
        if os.path.exists(tmp_dir):
            shutil.rmtree(tmp_dir)
        zip_ref.extractall(tmp_dir)

    extracted_folder = next(os.scandir(tmp_dir)).path

    print("Replacing files...")
    for item in os.listdir(extracted_folder):
        s = os.path.join(extracted_folder, item)
        d = os.path.join(".", item)

        if os.path.isdir(s):
            if os.path.exists(d):
                shutil.rmtree(d)
            shutil.copytree(s, d)
        else:
            shutil.copy2(s, d)

    shutil.rmtree(tmp_dir)

    print("Update complete! Restarting HessOS now...")

    python = sys.executable
    os.execv(python, [python] + sys.argv)
