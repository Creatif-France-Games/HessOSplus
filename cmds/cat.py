def run(args):
    if not args:
        print("Usage: cat <filename>")
        return

    filename = args[0]
    try:
        with open(filename, "r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("Error reading file:", e)
