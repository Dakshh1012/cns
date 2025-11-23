"""
Playfair Cipher - Digraph substitution cipher
Works with 5x5 matrix and encrypts pairs of letters
"""

def prepare_text(text):
    """Remove spaces and convert to uppercase"""
    return text.replace(" ", "").upper()

def create_playfair_matrix(key):
    """Create 5x5 playfair matrix from key"""
    key = prepare_text(key)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # I/J treated as same
    
    matrix = []
    seen = set()
    
    # Add key letters
    for char in key:
        if char not in seen and char in alphabet:
            matrix.append(char)
            seen.add(char)
    
    # Add remaining alphabet
    for char in alphabet:
        if char not in seen:
            matrix.append(char)
            seen.add(char)
    
    # Convert to 5x5 grid
    grid = [matrix[i:i+5] for i in range(0, 25, 5)]
    return grid

def find_position(grid, char):
    """Find row and column of character in grid"""
    for i in range(5):
        for j in range(5):
            if grid[i][j] == char:
                return i, j
    return None

def encrypt_playfair(text, key):
    """Encrypt using playfair cipher"""
    grid = create_playfair_matrix(key)
    text = prepare_text(text).replace('J', 'I')
    
    # Add filler if odd length
    if len(text) % 2 != 0:
        text += 'X'
    
    result = ""
    
    # Process pairs
    for i in range(0, len(text), 2):
        char1, char2 = text[i], text[i+1]
        row1, col1 = find_position(grid, char1)
        row2, col2 = find_position(grid, char2)
        
        if row1 == row2:  # Same row
            result += grid[row1][(col1 + 1) % 5]
            result += grid[row2][(col2 + 1) % 5]
        elif col1 == col2:  # Same column
            result += grid[(row1 + 1) % 5][col1]
            result += grid[(row2 + 1) % 5][col2]
        else:  # Rectangle
            result += grid[row1][col2]
            result += grid[row2][col1]
    
    return result

def decrypt_playfair(text, key):
    """Decrypt using playfair cipher"""
    grid = create_playfair_matrix(key)
    text = prepare_text(text)
    
    result = ""
    
    # Process pairs
    for i in range(0, len(text), 2):
        char1, char2 = text[i], text[i+1]
        row1, col1 = find_position(grid, char1)
        row2, col2 = find_position(grid, char2)
        
        if row1 == row2:  # Same row
            result += grid[row1][(col1 - 1) % 5]
            result += grid[row2][(col2 - 1) % 5]
        elif col1 == col2:  # Same column
            result += grid[(row1 - 1) % 5][col1]
            result += grid[(row2 - 1) % 5][col2]
        else:  # Rectangle
            result += grid[row1][col2]
            result += grid[row2][col1]
    
    return result

def playfair_menu():
    """Menu-driven playfair cipher operations"""
    while True:
        print("\n=== PLAYFAIR CIPHER ===")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        
        choice = input("Enter choice (1-3): ").strip()
        
        if choice == '1':
            text = input("Enter plaintext: ").strip()
            key = input("Enter key: ").strip()
            encrypted = encrypt_playfair(text, key)
            print(f"Encrypted: {encrypted}")
        
        elif choice == '2':
            text = input("Enter ciphertext: ").strip()
            key = input("Enter key: ").strip()
            decrypted = decrypt_playfair(text, key)
            print(f"Decrypted: {decrypted}")
        
        elif choice == '3':
            break
        
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    playfair_menu()
