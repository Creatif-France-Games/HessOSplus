import os

def run(args):
    if not args:
        print("Usage: cd <path>")
        return
    try:
        os.chdir(args[0])
    except FileNotFoundError:
        print("Directory not found.")
    except Exception as e:
        print("Error:", e)
