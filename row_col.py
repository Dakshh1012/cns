def columnar_encrypt():
    text = input("Enter plaintext: ")
    key = input("Enter key (word): ")

    text = text.replace(" ", "").lower()
    key = key.lower()

    key_order = sorted(list(key))          # alphabetical ordering of key
    cols = len(key)

    # build matrix row-wise
    rows = []
    for i in range(0, len(text), cols):
        rows.append(text[i:i + cols])

    print("\nMatrix:")
    for r in rows:
        print(r)

    cipher = ""
    # read columns according to key alphabetical order
    for ch in key_order:
        col = key.index(ch)
        for r in rows:
            if col < len(r):
                cipher += r[col]

    print("\nCiphertext:", cipher)


columnar_encrypt()