"""
Caesar Cipher - Simple substitution cipher
Shifts each letter by a fixed number of positions
"""

def encrypt_caesar(text, shift):
    """Encrypt text using Caesar cipher"""
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char
    return result

def decrypt_caesar(text, shift):
    """Decrypt text using Caesar cipher"""
    return encrypt_caesar(text, -shift)

def caesar_menu():
    """Menu-driven Caesar cipher operations"""
    while True:
        print("\n=== CAESAR CIPHER ===")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        
        choice = input("Enter choice (1-3): ").strip()
        
        if choice == '1':
            text = input("Enter plaintext: ").strip()
            shift = int(input("Enter shift value (1-25): ").strip())
            encrypted = encrypt_caesar(text, shift)
            print(f"Encrypted: {encrypted}")
        
        elif choice == '2':
            text = input("Enter ciphertext: ").strip()
            shift = int(input("Enter shift value (1-25): ").strip())
            decrypted = decrypt_caesar(text, shift)
            print(f"Decrypted: {decrypted}")
        
        elif choice == '3':
            break
        
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    caesar_menu()
