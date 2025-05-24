import os

def run(args):
    log_file = os.path.join(os.getcwd(), "logs", "os.log")
    if not os.path.exists(log_file):
        print("No logs found.")
        return

    with open(log_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
        # Optionnel : afficher les 20 dernières lignes
        for line in lines[-20:]:
            print(line, end="")
