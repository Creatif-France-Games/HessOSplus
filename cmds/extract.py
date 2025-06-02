import zipfile
import os

def main(args):
    if not args:
        print("Usage: extract <file.zip>")
        return

    zip_path = args[0]
    if not os.path.isfile(zip_path) or not zip_path.endswith(".zip"):
        print("Error: invalid or non-existent file.")
        return

    extract_folder = os.path.splitext(zip_path)[0]
    os.makedirs(extract_folder, exist_ok=True)

    with zipfile.ZipFile(zip_path, 'r') as zipf:
        zipf.extractall(extract_folder)

    print(f"✅ Extraction completed into: {extract_folder}/")