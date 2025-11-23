"""
Diffie-Hellman Key Exchange with Dual Server Socket Communication
Two independent servers on ports 5000 and 5001
Alice and Bob establish shared secret over insecure channel
"""

import socket
import threading
import time

def is_prime(n):
    """Check if a number is prime"""
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

def gcd(a, b):
    """Calculate GCD using Euclidean algorithm"""
    while b:
        a, b = b, a % b
    return a

def is_primitive_root(g, p):
    """Check if g is a primitive root modulo p"""
    if gcd(g, p) != 1:
        return False
    
    phi = p - 1
    factors = []
    temp = phi
    d = 2
    
    while d * d <= temp:
        while temp % d == 0:
            if not factors or factors[-1] != d:
                factors.append(d)
            temp //= d
        d += 1
    
    if temp > 1:
        factors.append(temp)
    
    for factor in factors:
        if pow(g, phi // factor, p) == 1:
            return False
    
    return True

def find_primitive_root(p):
    """Find a primitive root for prime p"""
    for g in range(2, p):
        if is_primitive_root(g, p):
            return g
    return None

class DHServer:
    """Diffie-Hellman Server for key exchange"""
    
    def __init__(self, username, port):
        self.username = username
        self.port = port
        self.p = None
        self.g = None
        self.private_key = None
        self.public_key = None
        self.server_socket = None
        self.client_socket = None
        self.other_public_key = None
        self.shared_secret = None
    
    def setup_parameters(self, p, g=None):
        """Setup DH parameters"""
        if not is_prime(p):
            print(f"Error: {p} is not prime!")
            return False
        
        self.p = p
        
        if g is None:
            g = find_primitive_root(p)
            if g is None:
                print("Could not find primitive root!")
                return False
        else:
            if not is_primitive_root(g, p):
                print(f"Warning: {g} may not be a primitive root")
        
        self.g = g
        print(f"\n✓ {self.username} DH parameters set: p={p}, g={g}")
        return True
    
    def generate_keys(self):
        """Generate DH keys"""
        if self.p is None or self.g is None:
            print("Setup parameters first!")
            return False
        
        import random
        self.private_key = random.randint(2, self.p - 2)
        self.public_key = pow(self.g, self.private_key, self.p)
        
        print(f"✓ {self.username} generated keys!")
        print(f"  Private Key: {self.private_key}")
        print(f"  Public Key: {self.public_key}")
        return True
    
    def start_server(self):
        """Start server on assigned port"""
        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server_socket.bind(('localhost', self.port))
            self.server_socket.listen(1)
            print(f"\n✓ {self.username} server started on port {self.port}")
            print(f"  Waiting for connection...")
        except Exception as err:
            print(f"Error starting server: {err}")
            return False
        
        return True
    
    def accept_connection(self):
        """Accept incoming connection"""
        try:
            self.client_socket, addr = self.server_socket.accept()
            print(f"✓ {self.username} accepted connection from {addr}")
            
            # Send DH parameters and public key
            data = f"{self.p}:{self.g}:{self.public_key}"
            self.client_socket.send(data.encode())
            
            # Receive other's public key
            other_data = self.client_socket.recv(1024).decode()
            self.other_public_key = int(other_data)
            print(f"✓ Received other user's public key: {self.other_public_key}")
            
            # Calculate shared secret
            self.shared_secret = pow(self.other_public_key, self.private_key, self.p)
            print(f"✓ Shared secret calculated: {self.shared_secret}")
            
            return True
        except Exception as err:
            print(f"Error accepting connection: {err}")
            return False
    
    def connect_to_other(self, other_port):
        """Connect to other server"""
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect(('localhost', other_port))
            print(f"✓ {self.username} connected to port {other_port}")
            
            # Receive DH parameters and public key
            data = self.client_socket.recv(1024).decode()
            p, g, other_pub = map(int, data.split(':'))
            
            # Use same p and g if already set, otherwise use received
            if self.p is None:
                self.p = p
                self.g = g
            
            self.other_public_key = other_pub
            print(f"✓ Received parameters: p={p}, g={g}")
            print(f"✓ Received other public key: {other_pub}")
            
            # Send public key
            self.client_socket.send(str(self.public_key).encode())
            
            # Calculate shared secret
            self.shared_secret = pow(self.other_public_key, self.private_key, self.p)
            print(f"✓ Shared secret calculated: {self.shared_secret}")
            
            return True
        except Exception as err:
            print(f"Error connecting: {err}")
            return False
    
    def display_info(self):
        """Display DH information"""
        print(f"\n--- {self.username} Information ---")
        if self.p and self.g:
            print(f"Parameters: p={self.p}, g={self.g}")
        if self.private_key:
            print(f"Private Key: {self.private_key}")
        if self.public_key:
            print(f"Public Key: {self.public_key}")
        if self.other_public_key:
            print(f"Other's Public Key: {self.other_public_key}")
        if self.shared_secret:
            print(f"Shared Secret: {self.shared_secret}")
    
    def close(self):
        """Close connections"""
        if self.client_socket:
            self.client_socket.close()
        if self.server_socket:
            self.server_socket.close()
        print(f"✓ {self.username} closed connection")

def dh_dual_server_menu():
    """Diffie-Hellman with dual independent servers"""
    alice = None
    bob = None
    
    while True:
        print("\n" + "="*70)
        print("DIFFIE-HELLMAN KEY EXCHANGE - DUAL SERVER")
        print("="*70)
        print("\n[SETUP]")
        print("1. Setup Alice (Port 5000)")
        print("2. Setup Bob (Port 5001)")
        print("3. Setup Alice DH Parameters")
        print("4. Setup Bob DH Parameters")
        print("\n[KEY GENERATION]")
        print("5. Alice Generate Keys")
        print("6. Bob Generate Keys")
        print("\n[CONNECTION & EXCHANGE]")
        print("7. Alice Starts Server (Port 5000)")
        print("8. Bob Starts Server (Port 5001)")
        print("9. Alice Connects to Bob (Port 5001)")
        print("10. Bob Connects to Alice (Port 5000)")
        print("\n[DISPLAY]")
        print("11. Display Alice Info")
        print("12. Display Bob Info")
        print("13. Exit")
        
        choice = input("\nEnter choice (1-13): ").strip()
        
        if choice == '1':
            alice = DHServer("Alice", 5000)
            print("✓ Alice initialized")
        
        elif choice == '2':
            bob = DHServer("Bob", 5001)
            print("✓ Bob initialized")
        
        elif choice == '3':
            if alice is None:
                print("Initialize Alice first!")
                continue
            
            try:
                print("\n--- Setup Alice DH Parameters ---")
                p = int(input("Enter prime p: ").strip())
                g_input = input("Enter primitive root g (press Enter for auto): ").strip()
                
                if g_input:
                    g = int(g_input)
                    alice.setup_parameters(p, g)
                else:
                    alice.setup_parameters(p)
            except ValueError:
                print("Invalid input!")
        
        elif choice == '4':
            if bob is None:
                print("Initialize Bob first!")
                continue
            
            try:
                print("\n--- Setup Bob DH Parameters ---")
                p = int(input("Enter prime p: ").strip())
                g_input = input("Enter primitive root g (press Enter for auto): ").strip()
                
                if g_input:
                    g = int(g_input)
                    bob.setup_parameters(p, g)
                else:
                    bob.setup_parameters(p)
            except ValueError:
                print("Invalid input!")
        
        elif choice == '5':
            if alice is None:
                print("Initialize Alice first!")
                continue
            alice.generate_keys()
        
        elif choice == '6':
            if bob is None:
                print("Initialize Bob first!")
                continue
            bob.generate_keys()
        
        elif choice == '7':
            if alice is None:
                print("Initialize Alice first!")
                continue
            
            if alice.start_server():
                def alice_accept():
                    alice.accept_connection()
                
                thread = threading.Thread(target=alice_accept, daemon=True)
                thread.start()
        
        elif choice == '8':
            if bob is None:
                print("Initialize Bob first!")
                continue
            
            if bob.start_server():
                def bob_accept():
                    bob.accept_connection()
                
                thread = threading.Thread(target=bob_accept, daemon=True)
                thread.start()
        
        elif choice == '9':
            if alice is None:
                print("Initialize Alice first!")
                continue
            
            print("Alice connecting to Bob on port 5001...")
            time.sleep(1)
            alice.connect_to_other(5001)
        
        elif choice == '10':
            if bob is None:
                print("Initialize Bob first!")
                continue
            
            print("Bob connecting to Alice on port 5000...")
            time.sleep(1)
            bob.connect_to_other(5000)
        
        elif choice == '11':
            if alice is None:
                print("Initialize Alice first!")
                continue
            alice.display_info()
        
        elif choice == '12':
            if bob is None:
                print("Initialize Bob first!")
                continue
            bob.display_info()
        
        elif choice == '13':
            if alice:
                alice.close()
            if bob:
                bob.close()
            print("\nGoodbye!")
            break
        
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    dh_dual_server_menu()
