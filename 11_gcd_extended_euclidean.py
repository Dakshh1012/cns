def extended_euclidean(a, b):
    """Extended Euclidean Algorithm with Bezout coefficients
    Returns (GCD, s, t) where a*s + b*t = gcd
    and shows table with s1, s2, t1, t2, s, t columns
    """
    original_a = a
    original_b = b
    
    if a < b:
        a, b = b, a
    
    # Initialize
    r1, r2 = a, b
    s1, s2 = 1, 0
    t1, t2 = 0, 1
    
    print("\n   Q     R1     R2      R    S1     S2      S    T1     T2      T")
    print("-" * 70)
    
    while r2 != 0:
        q = r1 // r2
        r = r1 % r2
        s = s1 - q * s2
        t = t1 - q * t2
        
        print(f"{q:4d} {r1:6d} {r2:6d} {r:6d} {s1:5d} {s2:5d} {s:6d} {t1:5d} {t2:5d} {t:6d}")
        
        r1, r2 = r2, r
        s1, s2 = s2, s
        t1, t2 = t2, t
    
    gcd = r1
    s = s1
    t = t1
    
    # Verify Bezout identity
    print(f"\nBezout Identity Verification:")
    print(f"{original_a} × {s} + {original_b} × {t} = {original_a * s + original_b * t}")
    
    return gcd, s, t


def extended_gcd_menu():
    while True:
        print("\n=== GCD USING EXTENDED EUCLIDEAN ALGORITHM ===")
        print("1. Find GCD and Bezout Coefficients")
        print("2. Exit")
        
        choice = input("Enter choice (1-2): ").strip()

        if choice == '1':
            try:
                a = int(input("Enter first number (a): ").strip())
                b = int(input("Enter second number (b): ").strip())

                if a < 0 or b < 0:
                    print("Please enter positive numbers!")
                    continue

                gcd_val, s, t = extended_euclidean(a, b)
                print(f"\nGCD({a}, {b}) = {gcd_val}")
                print(f"Bezout Coefficients: s = {s}, t = {t}")
                print(f"Verification: {a} × {s} + {b} × {t} = {gcd_val}")

            except ValueError:
                print("Invalid input! Enter integers only.")

        elif choice == '2':
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    extended_gcd_menu()