"""
Rail Fence Cipher - Encrypts plaintext using zigzag pattern (3 rails)
"""

def encrypt_rail_fence(text, rails=3):
    if rails <= 1:
        return text

    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1

    for char in text:
        fence[rail].append(char)

        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1

        rail += direction

    return "".join("".join(r) for r in fence)


def decrypt_rail_fence(cipher, rails=3):
    if rails <= 1:
        return cipher

    # determine zigzag pattern
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1
    for _ in cipher:
        fence[rail].append(None)
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        rail += direction

    # fill characters into pattern slots
    index = 0
    for r in range(rails):
        for j in range(len(fence[r])):
            fence[r][j] = cipher[index]
            index += 1

    # read following zigzag order
    result = []
    rail = 0
    direction = 1
    rail_pos = [0] * rails

    for _ in cipher:
        result.append(fence[rail][rail_pos[rail]])
        rail_pos[rail] += 1

        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1

        rail += direction

    return "".join(result)


def menu():
    while True:
        print("\n=== SINGLE RAIL FENCE (3 RAILS) ===")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")

        choice = input("Enter choice (1-3): ").strip()

        if choice == '1':
            text = input("Enter plaintext: ").strip()
            encrypted = encrypt_rail_fence(text, 3)
            print("Encrypted:", encrypted)

        elif choice == '2':
            text = input("Enter ciphertext: ").strip()
            decrypted = decrypt_rail_fence(text, 3)
            print("Decrypted:", decrypted)

        elif choice == '3':
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    menu()