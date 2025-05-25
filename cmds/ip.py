import socket

def run(args):
    try:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        print(f"IP address: {ip}")
    except Exception as e:
        print(f"Error: {e}")
