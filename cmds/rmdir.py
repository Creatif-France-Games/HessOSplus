import shutil

def run(args):
    if not args:
        print("Usage: rmdir <folder>")
        return
    try:
        shutil.rmtree(args[0])
        print(f"Deleted folder {args[0]}")
    except FileNotFoundError:
        print("Folder not found.")
    except Exception as e:
        print("Error:", e)
