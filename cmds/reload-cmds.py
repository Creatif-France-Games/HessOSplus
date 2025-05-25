# cmds/reload-cmds.py

import importlib
import os
import sys

def run(args):
    cmds_dir = os.path.join(os.path.dirname(__file__))

    loaded = []
    skipped = []

    for filename in os.listdir(cmds_dir):
        if filename.endswith(".py") and filename != "__init__.py":
            mod_name = f"cmds.{filename[:-3]}"
            try:
                if mod_name in sys.modules:
                    importlib.reload(sys.modules[mod_name])
                else:
                    importlib.import_module(mod_name)
                loaded.append(filename)
            except Exception as e:
                skipped.append((filename, str(e)))

    print(f"Reloaded {len(loaded)} command(s): {', '.join(loaded)}")
    if skipped:
        print("Skipped due to errors:")
        for file, err in skipped:
            print(f" - {file}: {err}")
