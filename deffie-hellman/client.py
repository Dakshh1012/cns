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
    # Connect to server
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((HOST, PORT))
    except ConnectionRefusedError:
        print(f"[ERROR] Cannot connect to {HOST}:{PORT}. Is the server running?")
        return
    print(f"[CLIENT] Connected to {HOST}:{PORT}")

    # Receive p and g from server
    data = client.recv(1024).decode()
    p, g = map(int, data.split(","))
    
    # Validate received parameters
    if not is_prime(p):
        print(f"[ERROR] Received p = {p} is not prime")
        client.close()
        return
    if p <= 5:
        print(f"[ERROR] Received p = {p} is too small (must be > 5)")
        client.close()
        return
    
    print(f"[CLIENT] Received p = {p}, g = {g}")

    # Ask user if they want random private key or manual entry
    choice = input("Generate private key automatically? (y/n): ").lower()
    if choice == "y":
        b = random.randint(2, p - 2)
    else:
        b = int(input("Enter private key b (between 2 and p-2): "))

    B = pow(g, b, p)
    print(f"[CLIENT] Private b = {b}, Public B = {B}")

    # Send B
    client.send(str(B).encode())

    # Receive A
    A = int(client.recv(1024).decode())
    print(f"[CLIENT] Received A = {A}")

    # Shared key
    K = pow(A, b, p)
    print(f"[CLIENT] Shared secret K = {K}")

    client.close()

if __name__ == "__main__":
    main()