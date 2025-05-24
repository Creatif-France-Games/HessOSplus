def run(args):
    if not args:
        print("Usage: touch <filename>")
        return

    filename = args[0]
    try:
        with open(filename, "w", encoding="utf-8"):
            pass
        print(f"File '{filename}' created.")
    except Exception as e:
        print("Error:", e)
