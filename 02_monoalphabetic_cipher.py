"""
Monoalphabetic Cipher - Substitution cipher with a random key
Each letter maps to a unique different letter
"""

def encrypt_monoalphabetic(text, key):
    """Encrypt using monoalphabetic cipher
    key: mapping dictionary {a->x, b->y, ...}
    """
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += key.get(char.lower(), char).upper()
            else:
                result += key.get(char, char)
        else:
            result += char
    return result

def decrypt_monoalphabetic(text, key):
    """Decrypt using monoalphabetic cipher
    Reverse the key mapping
    """
    reverse_key = {v: k for k, v in key.items()}
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += reverse_key.get(char.lower(), char).upper()
            else:
                result += reverse_key.get(char, char)
        else:
            result += char
    return result

def generate_monoalphabetic_key():
    """Generate a random monoalphabetic key"""
    import random
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shuffled = list(alphabet)
    random.shuffle(shuffled)
    return {alphabet[i]: shuffled[i] for i in range(26)}

def monoalphabetic_menu():
    """Menu-driven monoalphabetic cipher operations"""
    key = None
    
    while True:
        print("\n=== MONOALPHABETIC CIPHER ===")
        print("1. Generate New Key")
        print("2. Encrypt")
        print("3. Decrypt")
        print("4. Display Current Key")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ").strip()
        
        if choice == '1':
            key = generate_monoalphabetic_key()
            print("Key generated successfully!")
        
        elif choice == '2':
            if key is None:
                print("Please generate a key first!")
                continue
            text = input("Enter plaintext: ").strip()
            encrypted = encrypt_monoalphabetic(text, key)
            print(f"Encrypted: {encrypted}")
        
        elif choice == '3':
            if key is None:
                print("Please generate a key first!")
                continue
            text = input("Enter ciphertext: ").strip()
            decrypted = decrypt_monoalphabetic(text, key)
            print(f"Decrypted: {decrypted}")
        
        elif choice == '4':
            if key is None:
                print("No key generated yet!")
            else:
                print("\nCurrent Key Mapping:")
                for plain, cipher in sorted(key.items()):
                    print(f"{plain} -> {cipher}", end="  ")
                print()
        
        elif choice == '5':
            break
        
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    monoalphabetic_menu()
