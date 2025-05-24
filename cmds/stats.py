import os
import time

def run(args):
    if not args:
        print("Usage: stat <filename>")
        return

    path = args[0]
    try:
        stats = os.stat(path)
        print(f"File: {path}")
        print(f"Size: {stats.st_size} bytes")
        print(f"Created: {time.ctime(stats.st_ctime)}")
        print(f"Modified: {time.ctime(stats.st_mtime)}")
        print(f"Accessed: {time.ctime(stats.st_atime)}")
    except FileNotFoundError:
        print("File or folder not found.")
    except Exception as e:
        print("Error:", e)
