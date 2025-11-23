"""
Diffie-Hellman Key Exchange - Public key exchange algorithm
Allows two parties to establish a shared secret over an insecure channel
"""

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
    
    # Find all prime factors of p-1
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
    
    # Check if g^((p-1)/factor) != 1 for all prime factors
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

def diffie_hellman_setup(p, g=None):
    """Setup Diffie-Hellman parameters
    Returns: (p, g) where p is prime and g is primitive root
    """
    if not is_prime(p):
        raise ValueError(f"{p} is not prime!")
    
    if g is None:
        g = find_primitive_root(p)
        if g is None:
            raise ValueError("Could not find primitive root!")
    else:
        if not is_primitive_root(g, p):
            print(f"Warning: {g} may not be a primitive root of {p}")
    
    return p, g

def diffie_hellman_private_key(p):
    """Generate private key for DH"""
    import random
    return random.randint(2, p - 2)

def diffie_hellman_public_key(g, x, p):
    """Calculate public key given private key
    Public Key Y = g^X mod p
    """
    return pow(g, x, p)

def diffie_hellman_shared_secret(public_key, private_key, p):
    """Calculate shared secret
    Shared Secret = Y^X mod p
    """
    return pow(public_key, private_key, p)

def diffie_hellman_menu():
    """Menu-driven Diffie-Hellman key exchange"""
    p = None
    g = None
    alice_private = None
    bob_private = None
    
    while True:
        print("\n=== DIFFIE-HELLMAN KEY EXCHANGE ===")
        print("1. Setup Parameters (p and g)")
        print("2. Generate Keys for Alice and Bob")
        print("3. Exchange Public Keys and Calculate Shared Secret")
        print("4. Display Keys and Secret")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ").strip()
        
        if choice == '1':
            try:
                p = int(input("Enter prime p: ").strip())
                g_input = input("Enter primitive root g (press Enter for auto): ").strip()
                
                if g_input:
                    g = int(g_input)
                    p, g = diffie_hellman_setup(p, g)
                else:
                    p, g = diffie_hellman_setup(p)
                
                print(f"Parameters set: p={p}, g={g}")
            except ValueError as err:
                print(f"Error: {err}")
        
        elif choice == '2':
            if p is None or g is None:
                print("Please setup parameters first!")
                continue
            
            alice_private = diffie_hellman_private_key(p)
            bob_private = diffie_hellman_private_key(p)
            
            print("Keys generated for Alice and Bob!")
        
        elif choice == '3':
            if alice_private is None or bob_private is None:
                print("Please generate keys first!")
                continue
            
            alice_public = diffie_hellman_public_key(g, alice_private, p)
            bob_public = diffie_hellman_public_key(g, bob_private, p)
            
            alice_secret = diffie_hellman_shared_secret(bob_public, alice_private, p)
            bob_secret = diffie_hellman_shared_secret(alice_public, bob_private, p)
            
            print(f"\nAlice's Public Key: {alice_public}")
            print(f"Bob's Public Key: {bob_public}")
            print(f"\nAlice's Shared Secret: {alice_secret}")
            print(f"Bob's Shared Secret: {bob_secret}")
            print(f"Secrets Match: {alice_secret == bob_secret}")
        
        elif choice == '4':
            print("\n=== CURRENT STATE ===")
            print(f"Parameters: p={p}, g={g}")
            if alice_private:
                print(f"Alice's Private Key: {alice_private}")
                print(f"Bob's Private Key: {bob_private}")
            else:
                print("No private keys generated yet!")
        
        elif choice == '5':
            break
        
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    diffie_hellman_menu()
