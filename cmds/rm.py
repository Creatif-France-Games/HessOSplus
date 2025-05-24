import os

def run(args):
    if not args:
        print("Usage: rm <filename>")
        return
    try:
        os.remove(args[0])
        print(f"Deleted {args[0]}")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("Error:", e)
