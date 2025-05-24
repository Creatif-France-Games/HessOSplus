import importlib
from utils import logger

def handle_command(command_line):
    parts = command_line.strip().split()
    if not parts:
        return

    cmd, *args = parts
    try:
        module = importlib.import_module(f"cmds.{cmd}")
        module.run(args)
        logger.log(f"Command executed: {command_line}")
    except ModuleNotFoundError:
        print(f"Unknown command: {cmd}")
        logger.log(f"Unknown command attempted: {cmd}")
    except AttributeError:
        print(f"Command '{cmd}' does not implement a 'run' function.")
        logger.log(f"Command '{cmd}' missing 'run' function.")
    except Exception as e:
        print(f"Error running command '{cmd}': {e}")
        logger.log(f"Error in command '{command_line}': {e}")
