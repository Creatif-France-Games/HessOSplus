import os

def run(args):
    if len(args) < 2:
        print("Usage: rename <oldname> <newname>")
        return
    try:
        os.rename(args[0], args[1])
        print(f"{args[0]} renamed to {args[1]}")
    except FileNotFoundError:
        print("File or folder not found.")
    except Exception as e:
        print("Error:", e)
