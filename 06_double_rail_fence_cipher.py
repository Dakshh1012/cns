def rail_encrypt(text, rows=3):
    rails = [""] * rows
    rail = 0
    direction = 1

    for ch in text:
        rails[rail] += ch
        rail += direction

        # reverse direction at top and bottom rails
        if rail == rows - 1 or rail == 0:
            direction *= -1

    return "".join(rails)


def rail_decrypt(cipher, rows=3):
    # Build zigzag rail pattern
    pattern = []
    rail = 0
    direction = 1
    for _ in cipher:
        pattern.append(rail)
        rail += direction
        if rail == rows - 1 or rail == 0:
            direction *= -1

    # Count chars in each rail
    rail_count = [pattern.count(r) for r in range(rows)]

    # Slice cipher into rails
    rails = []
    idx = 0
    for count in rail_count:
        rails.append(cipher[idx:idx + count])
        idx += count

    # Rebuild message
    pointers = [0] * rows
    result = ""
    for r in pattern:
        result += rails[r][pointers[r]]
        pointers[r] += 1

    return result


def double_encrypt(text):
    first = rail_encrypt(text, 3)
    second = rail_encrypt(first, 3)
    return second


def double_decrypt(cipher):
    first = rail_decrypt(cipher, 3)
    second = rail_decrypt(first, 3)
    return second


def menu():
    while True:
        print("\n=== DOUBLE RAIL FENCE (3 ROWS) ===")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Enter choice (1-3): ")

        if choice == '1':
            text = input("Enter plaintext: ").strip()
            print("Encrypted:", double_encrypt(text))

        elif choice == '2':
            text = input("Enter ciphertext: ").strip()
            print("Decrypted:", double_decrypt(text))

        elif choice == '3':
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    menu()