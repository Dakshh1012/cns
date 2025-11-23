"""
Double Rail Fence Cipher - Enhanced transposition cipher
Uses two rails with improved security
"""

def encrypt_double_rail_fence(text, key):
    """Encrypt using double rail fence with key-based columnar transposition"""
    # First: Apply rail fence with 2 rails
    fence = [[], []]
    rail = 0
    
    for char in text:
        fence[rail].append(char)
        rail = 1 - rail
    
    combined = "".join(fence[0]) + "".join(fence[1])
    
    # Second: Apply columnar transposition with key
    cols = len(key)
    rows = (len(combined) + cols - 1) // cols
    
    # Pad if necessary
    while len(combined) < rows * cols:
        combined += 'X'
    
    # Create grid
    grid = [combined[i:i+cols] for i in range(0, len(combined), cols)]
    
    # Sort columns by key
    key_order = sorted(range(len(key)), key=lambda i: key[i])
    result = ""
    
    for order in key_order:
        for row in grid:
            if order < len(row):
                result += row[order]
    
    return result

def decrypt_double_rail_fence(text, key):
    """Decrypt using double rail fence with key-based columnar transposition"""
    cols = len(key)
    rows = len(text) // cols
    
    # Reconstruct grid from ciphertext using key order
    key_order = sorted(range(len(key)), key=lambda i: key[i])
    reverse_order = [0] * len(key_order)
    for i, j in enumerate(key_order):
        reverse_order[j] = i
    
    # Build grid
    grid = [[''] * cols for _ in range(rows)]
    index = 0
    
    for order in key_order:
        for row in range(rows):
            grid[row][order] = text[index]
            index += 1
    
    # Read row by row
    combined = "".join("".join(row) for row in grid)
    
    # Reverse rail fence
    mid = len(combined) // 2
    first_rail = combined[:mid]
    second_rail = combined[mid:]
    
    result = ""
    for i in range(max(len(first_rail), len(second_rail))):
        if i < len(first_rail):
            result += first_rail[i]
        if i < len(second_rail):
            result += second_rail[i]
    
    return result

def double_rail_fence_menu():
    """Menu-driven double rail fence cipher operations"""
    while True:
        print("\n=== DOUBLE RAIL FENCE CIPHER ===")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        
        choice = input("Enter choice (1-3): ").strip()
        
        if choice == '1':
            text = input("Enter plaintext: ").strip()
            key = input("Enter key (letters for ordering): ").strip()
            encrypted = encrypt_double_rail_fence(text, key)
            print(f"Encrypted: {encrypted}")
        
        elif choice == '2':
            text = input("Enter ciphertext: ").strip()
            key = input("Enter key (same as encryption): ").strip()
            decrypted = decrypt_double_rail_fence(text, key)
            print(f"Decrypted: {decrypted}")
        
        elif choice == '3':
            break
        
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    double_rail_fence_menu()
