import socket
import random

# Public parameters (same as server)
p = 23
g = 5

HOST = "127.0.0.1"
PORT = 5000

def main():
    # 1. Create TCP socket and connect to server
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    print(f"[CLIENT] Connected to {HOST}:{PORT}")

    # 2. Client chooses private key b
    b = random.randint(2, p-2)
    B = pow(g, b, p)   # B = g^b mod p
    print(f"[CLIENT] Private b = {b}, Public B = {B}")

    # 3. Send B to server
    client.send(str(B).encode())
    print(f"[CLIENT] Sent B = {B}")

    # 4. Receive A from server
    data = client.recv(1024).decode()
    A = int(data)
    print(f"[CLIENT] Received A = {A}")

    # 5. Compute shared key: K = A^b mod p
    K = pow(A, b, p)
    print(f"[CLIENT] Shared secret K = {K}")

    client.close()

if __name__ == "__main__":
    main()