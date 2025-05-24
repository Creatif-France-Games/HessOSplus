import os

def run(args):
    if not args:
        print("Usage: mkdir <foldername>")
        return

    folder = args[0]
    try:
        os.mkdir(folder)
        print(f"Folder '{folder}' created.")
    except FileExistsError:
        print("Folder already exists.")
    except Exception as e:
        print("Error:", e)
