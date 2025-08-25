import socket
from mitmproxy.tools.main import mitmdump

def get_local_ip():
    try:
        # Connect to an external address to determine the local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # IP doesn't need to be reachable; this just triggers OS to pick the interface
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception:
        return "127.0.0.1"

if __name__ == "__main__":
    ip = get_local_ip()
    print(f"Your local IP address is: {ip}")
    print("Use this IP as the Host in your proxy settings (Port: 8080)\n")

    # Start mitmdump with your script
    mitmdump(["-s", "modify.py"])
