import time
import os

start_time_file = "config/uptime_start.txt"

def get_start_time():
    if not os.path.exists(start_time_file):
        with open(start_time_file, "w") as f:
            f.write(str(time.time()))
        return time.time()
    with open(start_time_file, "r") as f:
        return float(f.read().strip())

def format_duration(seconds):
    days = int(seconds // 86400)
    hours = int((seconds % 86400) // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    return f"{days}d {hours}h {minutes}m {seconds}s"

def run(args):
    start = get_start_time()
    now = time.time()
    duration = now - start
    print("System Uptime:", format_duration(duration))
