import os

def run(args):
    if not args:
        print("Usage: find <name>")
        return

    name = args[0].lower()
    found = False
    for root, dirs, files in os.walk(os.getcwd()):
        for item in dirs + files:
            if name in item.lower():
                print(os.path.join(root, item))
                found = True

    if not found:
        print("No files or folders found matching:", name)
