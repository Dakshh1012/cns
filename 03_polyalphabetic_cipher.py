"""
Polyalphabetic Cipher (Vigenere Cipher)
Uses multiple Caesar shifts based on a key
"""

def encrypt_polyalphabetic(text, key):
    """Encrypt using Vigenere cipher"""
    result = ""
    key_index = 0
    key = key.lower()
    
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            key_index += 1
        else:
            result += char
    
    return result

def decrypt_polyalphabetic(text, key):
    """Decrypt using Vigenere cipher"""
    result = ""
    key_index = 0
    key = key.lower()
    
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')
            if char.isupper():
                result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            key_index += 1
        else:
            result += char
    
    return result

def polyalphabetic_menu():
    """Menu-driven polyalphabetic cipher operations"""
    while True:
        print("\n=== POLYALPHABETIC CIPHER (VIGENERE) ===")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        
        choice = input("Enter choice (1-3): ").strip()
        
        if choice == '1':
            text = input("Enter plaintext: ").strip()
            key = input("Enter key (letters only): ").strip()
            encrypted = encrypt_polyalphabetic(text, key)
            print(f"Encrypted: {encrypted}")
        
        elif choice == '2':
            text = input("Enter ciphertext: ").strip()
            key = input("Enter key (letters only): ").strip()
            decrypted = decrypt_polyalphabetic(text, key)
            print(f"Decrypted: {decrypted}")
        
        elif choice == '3':
            break
        
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    polyalphabetic_menu()
