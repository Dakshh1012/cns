"""
RSA Encryption - Asymmetric encryption algorithm
Public key cryptography system
"""

def gcd(a, b):
    """Calculate GCD using Euclidean algorithm"""
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    """Find modular inverse of e mod phi using Extended Euclidean"""
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        gcd_val, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd_val, x, y
    
    _, x, _ = extended_gcd(e % phi, phi)
    return (x % phi + phi) % phi

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

def generate_rsa_keys(p, q, e=65537):
    """Generate RSA public and private keys
    p, q: prime numbers
    e: public exponent (default 65537)
    Returns: (public_key, private_key)
    """
    if not is_prime(p) or not is_prime(q):
        raise ValueError("p and q must be prime!")
    
    n = p * q
    phi = (p - 1) * (q - 1)
    
    if gcd(e, phi) != 1:
        raise ValueError("e and phi must be coprime!")
    
    d = mod_inverse(e, phi)
    
    return (e, n), (d, n)

def encrypt_rsa(plaintext, public_key):
    """Encrypt using RSA public key"""
    e, n = public_key
    # Convert string to number
    plaintext_num = int.from_bytes(plaintext.encode(), byteorder='big')
    ciphertext_num = pow(plaintext_num, e, n)
    return ciphertext_num

def decrypt_rsa(ciphertext_num, private_key):
    """Decrypt using RSA private key"""
    d, n = private_key
    plaintext_num = pow(ciphertext_num, d, n)
    # Convert number back to string
    plaintext = plaintext_num.to_bytes((plaintext_num.bit_length() + 7) // 8, byteorder='big').decode()
    return plaintext

def rsa_menu():
    """Menu-driven RSA operations"""
    public_key = None
    private_key = None
    
    while True:
        print("\n=== RSA ENCRYPTION ===")
        print("1. Generate RSA Keys")
        print("2. Encrypt")
        print("3. Decrypt")
        print("4. Display Keys")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ").strip()
        
        if choice == '1':
            try:
                p = int(input("Enter prime p: ").strip())
                q = int(input("Enter prime q: ").strip())
                e = int(input("Enter public exponent e (default 65537): ").strip() or "65537")
                
                public_key, private_key = generate_rsa_keys(p, q, e)
                print("Keys generated successfully!")
            except ValueError as err:
                print(f"Error: {err}")
        
        elif choice == '2':
            if public_key is None:
                print("Please generate keys first!")
                continue
            text = input("Enter plaintext: ").strip()
            try:
                ciphertext = encrypt_rsa(text, public_key)
                print(f"Encrypted (number): {ciphertext}")
            except Exception as err:
                print(f"Error: {err}")
        
        elif choice == '3':
            if private_key is None:
                print("Please generate keys first!")
                continue
            try:
                ciphertext = int(input("Enter ciphertext (number): ").strip())
                plaintext = decrypt_rsa(ciphertext, private_key)
                print(f"Decrypted: {plaintext}")
            except Exception as err:
                print(f"Error: {err}")
        
        elif choice == '4':
            if public_key and private_key:
                print(f"\nPublic Key (e, n): {public_key}")
                print(f"Private Key (d, n): ({private_key[0]}, {private_key[1]})")
            else:
                print("No keys generated yet!")
        
        elif choice == '5':
            break
        
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    rsa_menu()
