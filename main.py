from startup import boot
import time
import importlib
from startup.boot import clear_screen

def handle_command(command_line):
    parts = command_line.strip().split()
    if not parts:
        return
    cmd_name = parts[0]
    args = parts[1:]
    try:
        module = importlib.import_module(f"cmds.{cmd_name}")
        module.run(args)
    except ModuleNotFoundError:
        print(f"Unknown command: {cmd_name}")
    except Exception as e:
        print(f"Error running command '{cmd_name}': {e}")

def main():
    boot.boot()

    print("Welcome to HessOS V3")
    print("Type 'help' for a list of commands.")
    print(" --> Dont forget to star the repo : github.com/bowser-2077/HessOS")

    while True:
        command = input("| HessOS 3.0 | >> ").strip()
        if command.lower() in ("forceexit", "exit", "quit"):
            clear_screen()
            print("Bye!")
            time.sleep(1)
            break
        handle_command(command)

if __name__ == "__main__":
    main()
