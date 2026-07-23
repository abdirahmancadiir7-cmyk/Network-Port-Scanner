import socket
from datetime import datetime

print("=" * 50)
print("         NETWORK PORT SCANNER")
print("=" * 50)

target = input("Enter Target IP or Host: ")

start_port = int(input("Start Port: "))
end_port = int(input("End Port: "))

print(f"\nScanning {target}")
print(f"Started: {datetime.now()}\n")

for port in range(start_port, end_port + 1):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"[OPEN] Port {port}")

    sock.close()

print(f"\nFinished: {datetime.now()}")
