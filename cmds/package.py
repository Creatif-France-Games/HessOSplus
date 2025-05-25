import os
import json

CONFIG_FILE = "config/packages.json"
CMDS_DIR = "cmds"

def load_config():
    if not os.path.exists(CONFIG_FILE):
        return {}
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)

def run(args):
    if not args:
        print("Usage: package [install|uninstall|list] [package_name] [ignore-config]")
        return

    ignore_config = False
    if args[-1].lower() == "ignore-config":
        ignore_config = True
        args = args[:-1]

    if len(args) < 1:
        print("Usage: package [install|uninstall|list] [package_name] [ignore-config]")
        return

    action = args[0].lower()

    # Charge config uniquement si on ne l'ignore pas
    config = {}
    if not ignore_config:
        config = load_config()

    if action == "list":
        print("Available packages:")
        for file in os.listdir(CMDS_DIR):
            if file.endswith(".py.disabled"):
                name = file.replace(".py.disabled", "")
                if ignore_config or name in config.get("packages", []):
                    print(f"- {name} (can be installed)")
        return

    if len(args) < 2:
        print(f"Usage: package {action} <package_name> [ignore-config]")
        return

    pkg_name = args[1]
    pkg_file = os.path.join(CMDS_DIR, f"{pkg_name}.py")
    disabled_file = os.path.join(CMDS_DIR, f"{pkg_name}.py.disabled")

    if action == "install":
        if not os.path.exists(disabled_file):
            print(f"Package '{pkg_name}' is not available or already installed.")
            return
        if not ignore_config and pkg_name not in config.get("packages", []):
            print(f"Package '{pkg_name}' is not installable (not in config).")
            return
        os.rename(disabled_file, pkg_file)
        print(f"Package '{pkg_name}' installed.")
        return

    if action == "uninstall":
        if not os.path.exists(pkg_file):
            print(f"Package '{pkg_name}' is not installed.")
            return
        if not ignore_config and pkg_name not in config.get("packages", []):
            print(f"Package '{pkg_name}' cannot be uninstalled (not in config).")
            return
        os.rename(pkg_file, disabled_file)
        print(f"Package '{pkg_name}' uninstalled.")
        return

    print("Unknown action. Use install, uninstall or list.")
