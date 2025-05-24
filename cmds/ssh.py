import sys
import paramiko

def run(args):
    if len(args) < 3:
        print("Usage: ssh <host> <username> <password>")
        return

    host, username, password = args[0], args[1], args[2]
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(hostname=host, username=username, password=password)
        print(f"Connected to {host}")
        while True:
            cmd = input(f"{username}@{host}:~$ ")
            if cmd.lower() in ("exit", "quit"):
                break
            stdin, stdout, stderr = client.exec_command(cmd)
            print(stdout.read().decode())
            err = stderr.read().decode()
            if err:
                print("Error:", err)
    except Exception as e:
        print("Connection failed:", e)
    finally:
        client.close()
