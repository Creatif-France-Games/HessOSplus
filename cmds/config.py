from utils import config_manager

def run(args):
    config = config_manager.load_config()

    if not args:
        # Affiche la config entière
        if not config:
            print("Config is empty.")
        else:
            for k, v in config.items():
                print(f"{k} = {v}")
        return

    # Syntaxe : config set key value
    # ou      : config get key
    cmd = args[0].lower()

    if cmd == "set":
        if len(args) < 3:
            print("Usage: config set <key> <value>")
            return
        key = args[1]
        value = args[2]
        config[key] = value
        config_manager.save_config(config)
        print(f"Config updated: {key} = {value}")

    elif cmd == "get":
        if len(args) < 2:
            print("Usage: config get <key>")
            return
        key = args[1]
        value = config.get(key)
        if value is None:
            print(f"No value found for key '{key}'.")
        else:
            print(f"{key} = {value}")

    else:
        print("Unknown command. Use 'config get <key>' or 'config set <key> <value>'.")
