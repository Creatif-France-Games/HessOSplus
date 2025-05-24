import random
import time
import os

def run(args):
    chars = "01"
    try:
        for _ in range(30):
            line = "".join(random.choice(chars) for _ in range(80))
            print(line)
            time.sleep(0.05)
    except KeyboardInterrupt:
        pass
