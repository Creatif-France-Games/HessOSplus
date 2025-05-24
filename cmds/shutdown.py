import time
import os
import random
import shutil
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def shutdown_animation():
    clear_screen()
    cols, lines = shutil.get_terminal_size()
    total_services = 50
    duration = 3  # secondes
    delay = duration / total_services

    service_names = [f"{''.join(random.choices('WXCVBN', k=8))}.service" for _ in range(total_services)]

    for svc in service_names:
        # Sauvegarder la position du curseur
        print('\033[s', end='')
        # Aller à la dernière ligne, colonne 1
        print(f'\033[{lines};1H', end='')
        # Effacer la ligne entière
        print(' ' * cols, end='')
        # Aller à la position bas droite - longueur du texte
        print(f'\033[{lines};{cols - len(svc)}H', end='')
        # Afficher le nom du service
        print(svc, end='')
        # Restaurer la position du curseur
        print('\033[u', end='')
        sys.stdout.flush()
        time.sleep(delay)

    clear_screen()
    print("System is shutting down...")
    time.sleep(2)
    clear_screen()

def run(args):
    shutdown_animation()
    sys.exit()
    # Ici tu peux ajouter un exit si tu veux couper la boucle principale
    # import sys
    # sys.exit()

