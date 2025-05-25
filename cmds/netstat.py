import psutil

def run(args):
    connections = psutil.net_connections()
    for conn in connections[:10]:  # Limit to first 10 for brevity
        laddr = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "-"
        raddr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "-"
        print(f"{conn.status:>12} | {laddr:>21} -> {raddr:>21}")
