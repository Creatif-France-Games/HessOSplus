
from ftplib import FTP

def run(args):
    if len(args) < 3:
        print("Usage: ftp <host> <username> <password>")
        return
    try:
        ftp = FTP(args[0])
        ftp.login(args[1], args[2])
        print("Connected. Use 'ls', 'get <file>', or 'quit'.")
        while True:
            cmd = input("ftp> ").strip()
            if cmd == "quit":
                ftp.quit()
                break
            elif cmd == "ls":
                ftp.retrlines('LIST')
            elif cmd.startswith("get "):
                filename = cmd.split(" ", 1)[1]
                with open(filename, "wb") as f:
                    ftp.retrbinary(f"RETR {filename}", f.write)
                print(f"Downloaded {filename}")
            else:
                print("Unknown command.")
    except Exception as e:
        print(f"FTP error: {e}")
