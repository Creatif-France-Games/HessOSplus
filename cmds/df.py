
import shutil

def run(args):
    total, used, free = shutil.disk_usage("/")
    print(f"Total: {total // 1024**3} GB")
    print(f"Used: {used // 1024**3} GB")
    print(f"Free: {free // 1024**3} GB")
