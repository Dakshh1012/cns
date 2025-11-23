import socket
import random

# Public parameters (same on both sides)
p = 23          # prime
g = 5           # primitive root mod p

HOST = "127.0.0.1"
PORT = 5000

def main():
    # 1. Create TCP socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(1)
    print(f"[SERVER] Waiting for connection on {HOST}:{PORT} ...")

    conn, addr = server.accept()
    print(f"[SERVER] Connected by {addr}")

    # 2. Server chooses private key a
    a = random.randint(2, p-2)
    A = pow(g, a, p)  # A = g^a mod p
    print(f"[SERVER] Private a = {a}, Public A = {A}")

    # 3. Receive client's public key B
    data = conn.recv(1024).decode()
    B = int(data)
    print(f"[SERVER] Received B = {B}")

    # 4. Send A to client
    conn.send(str(A).encode())
    print(f"[SERVER] Sent A = {A}")

    # 5. Compute shared key: K = B^a mod p
    K = pow(B, a, p)
    print(f"[SERVER] Shared secret K = {K}")

    conn.close()
    server.close()

if __name__ == "__main__":
    main()