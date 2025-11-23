"""
Rail Fence Cipher - Transposition cipher
Writes plaintext in zigzag pattern across multiple rails
"""

def encrypt_rail_fence(text, rails):
    """Encrypt using rail fence cipher"""
    if rails <= 1:
        return text
    
    # Create rails
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1
    
    # Write text in zigzag
    for char in text:
        fence[rail].append(char)
        
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        
        rail += direction
    
    # Read off each rail
    result = ""
    for rail_list in fence:
        result += "".join(rail_list)
    
    return result

def decrypt_rail_fence(text, rails):
    """Decrypt using rail fence cipher"""
    if rails <= 1:
        return text
    
    # Calculate lengths for each rail
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1
    
    # Mark positions for each rail
    for i in range(len(text)):
        fence[rail].append(None)
        
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        
        rail += direction
    
    # Fill in characters from ciphertext
    index = 0
    for i in range(rails):
        for j in range(len(fence[i])):
            fence[i][j] = text[index]
            index += 1
    
    # Read zigzag to get plaintext
    result = []
    rail = 0
    direction = 1
    rail_indices = [0] * rails
    
    for i in range(len(text)):
        result.append(fence[rail][rail_indices[rail]])
        rail_indices[rail] += 1
        
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        
        rail += direction
    
    return "".join(result)

def rail_fence_menu():
    """Menu-driven rail fence cipher operations"""
    while True:
        print("\n=== RAIL FENCE CIPHER ===")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        
        choice = input("Enter choice (1-3): ").strip()
        
        if choice == '1':
            text = input("Enter plaintext: ").strip()
            rails = int(input("Enter number of rails: ").strip())
            encrypted = encrypt_rail_fence(text, rails)
            print(f"Encrypted: {encrypted}")
        
        elif choice == '2':
            text = input("Enter ciphertext: ").strip()
            rails = int(input("Enter number of rails: ").strip())
            decrypted = decrypt_rail_fence(text, rails)
            print(f"Decrypted: {decrypted}")
        
        elif choice == '3':
            break
        
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    rail_fence_menu()
