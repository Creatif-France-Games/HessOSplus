
import psutil

def run(args):
    mem = psutil.virtual_memory()
    print(f"Total: {mem.total // 1024**2} MB")
    print(f"Used: {mem.used // 1024**2} MB")
    print(f"Free: {mem.available // 1024**2} MB")
