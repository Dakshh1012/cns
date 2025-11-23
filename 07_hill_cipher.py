"""
Hill Cipher - Block cipher based on matrix operations
Uses matrices for encryption and decryption
"""

def matrix_mod_inverse(matrix, mod):
    """Calculate modular inverse of 2x2 matrix mod m"""
    a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
    
    det = (a * d - b * c) % mod
    
    # Find modular inverse of determinant
    for i in range(1, mod):
        if (det * i) % mod == 1:
            det_inv = i
            break
    else:
        raise ValueError("Matrix is not invertible!")
    
    # Inverse matrix
    inv_matrix = [
        [(d * det_inv) % mod, (-b * det_inv) % mod],
        [(-c * det_inv) % mod, (a * det_inv) % mod]
    ]
    
    return inv_matrix

def encrypt_hill_2x2(text, key_matrix, mod=26):
    """Encrypt using 2x2 Hill cipher
    key_matrix: 2x2 encryption matrix
    """
    text = text.upper().replace(" ", "")
    result = ""
    
    # Process pairs of letters
    if len(text) % 2 != 0:
        text += 'X'
    
    for i in range(0, len(text), 2):
        # Convert letters to numbers (A=0, B=1, ..., Z=25)
        p1 = ord(text[i]) - ord('A')
        p2 = ord(text[i+1]) - ord('A')
        
        # Matrix multiplication
        c1 = (key_matrix[0][0] * p1 + key_matrix[0][1] * p2) % mod
        c2 = (key_matrix[1][0] * p1 + key_matrix[1][1] * p2) % mod
        
        result += chr(c1 + ord('A')) + chr(c2 + ord('A'))
    
    return result

def decrypt_hill_2x2(text, key_matrix, mod=26):
    """Decrypt using 2x2 Hill cipher"""
    text = text.upper().replace(" ", "")
    inv_matrix = matrix_mod_inverse(key_matrix, mod)
    result = ""
    
    for i in range(0, len(text), 2):
        c1 = ord(text[i]) - ord('A')
        c2 = ord(text[i+1]) - ord('A')
        
        # Matrix multiplication with inverse
        p1 = (inv_matrix[0][0] * c1 + inv_matrix[0][1] * c2) % mod
        p2 = (inv_matrix[1][0] * c1 + inv_matrix[1][1] * c2) % mod
        
        result += chr(p1 + ord('A')) + chr(p2 + ord('A'))
    
    return result

def hill_cipher_menu():
    """Menu-driven Hill cipher operations"""
    print("\n=== HILL CIPHER (2x2) ===")
    print("Default key matrix:")
    print("[ 6  24 ]")
    print("[ 1  16 ]")
    key_matrix = [[6, 24], [1, 16]]
    
    while True:
        print("\n=== HILL CIPHER MENU ===")
        print("1. Encrypt (with default key)")
        print("2. Decrypt (with default key)")
        print("3. Set Custom Key Matrix")
        print("4. Exit")
        
        choice = input("Enter choice (1-4): ").strip()
        
        if choice == '1':
            text = input("Enter plaintext: ").strip()
            encrypted = encrypt_hill_2x2(text, key_matrix)
            print(f"Encrypted: {encrypted}")
        
        elif choice == '2':
            text = input("Enter ciphertext: ").strip()
            try:
                decrypted = decrypt_hill_2x2(text, key_matrix)
                print(f"Decrypted: {decrypted}")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == '3':
            try:
                print("Enter 2x2 key matrix:")
                a = int(input("a[0][0]: ").strip())
                b = int(input("a[0][1]: ").strip())
                c = int(input("a[1][0]: ").strip())
                d = int(input("a[1][1]: ").strip())
                key_matrix = [[a, b], [c, d]]
                print("Key matrix updated!")
            except ValueError:
                print("Invalid input!")
        
        elif choice == '4':
            break
        
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    hill_cipher_menu()
