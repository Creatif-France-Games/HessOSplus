from datetime import datetime

def run(args):
    now = datetime.now()
    print("Current time:", now.strftime("%H:%M:%S"))
