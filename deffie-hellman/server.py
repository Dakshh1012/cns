import socket
import random

HOST = "127.0.0.1"
PORT = 5000

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    # Ask user for public parameters
    while True:
        p = int(input("Enter prime number p (must be > 5): "))
        if p > 5 and is_prime(p):
            break
        print(f"[ERROR] {p} is not a valid prime or is too small. Use prime > 5")
    
    g = int(input("Enter primitive root g (1 < g < p): "))
    if not (1 < g < p):
        print(f"[ERROR] g must be between 1 and {p-1}")
        return

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(1)
    print(f"[SERVER] Waiting for connection on {HOST}:{PORT} ...")

    conn, addr = server.accept()
    print(f"[SERVER] Connected by {addr}")

    # Send p and g first
    conn.send(f"{p},{g}".encode())

    # Generate private key
    a = random.randint(2, p - 2)
    A = pow(g, a, p)
    print(f"[SERVER] Private a = {a}, Public A = {A}")

    # Receive B
    B = int(conn.recv(1024).decode())
    print(f"[SERVER] Received B = {B}")

    # Send A
    conn.send(str(A).encode())
    print(f"[SERVER] Sent A = {A}")

    # Shared key
    K = pow(B, a, p)
    print(f"[SERVER] Shared secret K = {K}")

    conn.close()
    server.close()

if __name__ == "__main__":
    main()