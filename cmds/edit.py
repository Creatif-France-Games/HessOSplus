def run(args):
    if not args:
        print("Usage: edit <filename>")
        return

    filename = args[0]
    print("Enter text (CTRL+Z then Enter to save on Windows, CTRL+D on Linux/macOS):")
    try:
        lines = []
        while True:
            try:
                line = input()
                lines.append(line)
            except EOFError:
                break
        with open(filename, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        print(f"{filename} saved.")
    except Exception as e:
        print("Error:", e)
