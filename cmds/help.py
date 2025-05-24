import os

def run(args):
    print("Available commands:")
    # On récupère le chemin absolu du dossier cmds par rapport à ce fichier
    cmds_path = os.path.join(os.path.dirname(__file__))
    files = os.listdir(cmds_path)
    commands = [f[:-3] for f in files if f.endswith(".py") and f != "__init__.py"]
    for cmd in sorted(commands):
        print(f" - {cmd}")
