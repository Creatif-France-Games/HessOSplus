import subprocess
import platform

def run(args):
    if not args:
        print("Usage: ping <host>")
        return

    host = args[0]
    param = "-n" if platform.system().lower() == "windows" else "-c"
    try:
        print(f"Pinging {host}...")
        result = subprocess.run(["ping", param, "4", host], capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print("Error:", e)
