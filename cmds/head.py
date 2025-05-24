def run(args):
    if not args:
        print("Usage: head <filename> [lines]")
        return

    filename = args[0]
    lines_to_show = int(args[1]) if len(args) > 1 else 10

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for _ in range(lines_to_show):
                line = f.readline()
                if not line:
                    break
                print(line.rstrip())
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("Error:", e)
