import os
import zipfile

def main(args):
    if not args:
        print("Usage: compress <file_or_folder_path>")
        return

    path = args[0]
    if not os.path.exists(path):
        print(f"Error: {path} does not exist.")
        return

    zip_name = os.path.basename(path.rstrip('/\\')) + ".zip"
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        if os.path.isdir(path):
            for root, _, files in os.walk(path):
                for file in files:
                    full_path = os.path.join(root, file)
                    arcname = os.path.relpath(full_path, path)
                    zipf.write(full_path, arcname)
        else:
            zipf.write(path, os.path.basename(path))

    print(f"✅ Compression completed: {zip_name}")