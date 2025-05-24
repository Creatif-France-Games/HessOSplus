import os

def run(args):
    path = args[0] if args else "."
    try:
        for item in os.listdir(path):
            print(item)
    except FileNotFoundError:
        print("Directory not found.")
