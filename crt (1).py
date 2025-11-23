def euclidean(a, b):
    if a > b:
        r1 = a
        r2 = b
    else:
        r1 = b
        r2 = a
    while r2 != 0:
        r1, r2 = r2, r1 % r2
    return r1


def mi(a, b):
    if a <= b:
        r1 = b
        r2 = a
    else:
        r1 = b
        r2 = a % b

    if euclidean(r1, r2) == 1:
        t1 = 0
        t2 = 1
        while r2 != 0:
            q = r1 // r2
            r = r1 % r2
            t = t1 - t2 * q
            r1 = r2
            r2 = r
            t1 = t2
            t2 = t
    else:
        print("MI is possible only for coprime numbers")
        exit()

    if t1 < 0:
        t1 += b
    return t1


def crt(c, m, k):
    M = 1
    for i in range(k):
        M *= m[i]

    M_val = []
    for i in range(k):
        M_val.append(M // m[i])

    Minv = []
    for i in range(k):
        Minv.append(mi(M_val[i], m[i]))

    cval = 0
    print("Residue Results:")
    for i in range(k):
        print(c[i])
        cval += (c[i] * M_val[i] * Minv[i]) % M

    return cval % M


def main():
    n1 = int(input("Enter a: "))
    n2 = int(input("Enter b: "))
    k = int(input("How many moduli: "))

    m = []
    for i in range(k):
        m.append(int(input(f"Enter pairwise coprime modulus {i+1}: ")))

    a = []
    b = []
    for i in range(k):
        a.append(n1 % m[i])
        b.append(n2 % m[i])

    print("\n1-Addition")
    print("2-Subtraction")
    print("3-Multiplication")
    print("4-Division")
    choice = int(input("Enter choice: "))

    c = []
    if choice == 1:
        for i in range(k):
            c.append((a[i] + b[i]) % m[i])
    elif choice == 2:
        for i in range(k):
            c.append((a[i] - b[i]) % m[i])
    elif choice == 3:
        for i in range(k):
            c.append((a[i] * b[i]) % m[i])
    elif choice == 4:
        for i in range(k):
            c.append((a[i] * mi(b[i], m[i])) % m[i])
    else:
        print("Invalid choice")
        return

    ans = crt(c, m, k)
    print("\nFinal Answer:", ans)


main()