import subprocess
import sys

def run(args):
    if not args:
        print("Usage: py <script.py>")
        return

    script = args[0]
    try:
        result = subprocess.run([sys.executable, script], capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print("Error:", result.stderr)
    except FileNotFoundError:
        print("Script not found.")
    except Exception as e:
        print("Error:", e)
