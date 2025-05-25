
import psutil

def run(args):
    print(f"{'PID':>6} {'Name':<25} {'CPU%':>6} {'Memory%':>8}")
    for p in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            print(f"{p.info['pid']:>6} {p.info['name'][:25]:<25} {p.info['cpu_percent']:>6.1f} {p.info['memory_percent']:>8.2f}")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
