# Calling for socket library
import socket

# Ask for IP
target = input("Enter target IP: ")

# Checking for IP validity
try:
    socket.inet_aton(target)
except socket.error:
    print("Invalid IP address!")
    exit()

# Scanning the inserted IP
print(f"\nScanning {target}...")
print("-" * 30)
found_open_port = False
for port in range(1, 1025):

    # Checking for TCP ports 
    # The socket.AF_INET is for IPv4 or IP address
    # The socket.SOCK_STREAM is for TCP
    tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_sock.settimeout(0.2)
    result = tcp_sock.connect_ex((target, port))
    # Receiving condition
    if result == 0:
        print(f"[+] TCP Port {port} is OPEN")
        found_open_port = True
    tcp_sock.close()

    # Checking for UDP ports
    # The socket.SOCK_DGRAM is for UDP
    udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_sock.settimeout(0.2)
    udp_sock.sendto(b"", (target, port))
    try:
        udp_sock.recvfrom(1024)
        print(f"[+] UDP Port {port} is OPEN")
        found_open_port = True
    # Time condition 
    except socket.timeout:
        pass
    udp_sock.close()

# If no port is open
if not found_open_port:
    print("No port is open!")
print("\nScan complete.")