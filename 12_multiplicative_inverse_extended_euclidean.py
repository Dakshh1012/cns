"""
Multiplicative Inverse using Extended Euclidean Algorithm
Finds the multiplicative inverse of a number modulo m
Formula: Find MI such that (a × MI) ≡ 1 (mod m)

Mathematical Basis:
If gcd(a, m) = 1 (coprime), then Extended Euclidean gives us: a*x + m*y = 1
Taking mod m: (a*x) mod m = 1
So x is the multiplicative inverse of a modulo m
"""

def euclidean(a, b):
    """Find GCD using Euclidean algorithm - checks if MI exists"""
    if a > b:
        r1 = a
        r2 = b
    else:
        r1 = b
        r2 = a
    
    while r2 != 0:
        q = r1 // r2
        r = r1 % r2
        r1 = r2
        r2 = r
    
    return r1

def multiplicative_inverse(a, m):
    """Find multiplicative inverse of a mod m using Extended Euclidean
    Returns: MI such that (a * MI) ≡ 1 (mod m)
    
    MI only exists if gcd(a, m) = 1 (a and m are coprime)
    """
    # Check if MI exists
    if euclidean(m, a) != 1:
        return None
    
    # Apply Extended Euclidean to find MI
    r1 = m
    r2 = a % m
    
    t1 = 0
    t2 = 1
    
    print(f"\n{'Q':<5} {'R1':<5} {'R2':<5} {'R':<5} {'T1':<5} {'T2':<5} {'T':<5}")
    print("-" * 50)
    
    while r2 != 0:
        q = r1 // r2
        r = r1 % r2
        t = t1 - t2 * q
        print(f"{q:<5} {r1:<5} {r2:<5} {r:<5} {t1:<5} {t2:<5} {t:<5}")
        r1 = r2
        r2 = r
        t1 = t2
        t2 = t
    
    mi = t1
    if mi < 0:
        mi += m
    
    return mi

def multiplicative_inverse_menu():
    """Menu-driven Multiplicative Inverse using Extended Euclidean"""
    while True:
        print("\n=== MULTIPLICATIVE INVERSE USING EXTENDED EUCLIDEAN ===")
        print("1. Find Multiplicative Inverse")
        print("2. Exit")
        
        choice = input("Enter choice (1-2): ").strip()
        
        if choice == '1':
            try:
                a = int(input("Enter number (a): ").strip())
                m = int(input("Enter modulus (m): ").strip())
                
                if a < 0 or m < 0:
                    print("Please enter positive numbers!")
                    continue
                
                mi = multiplicative_inverse(a, m)
                
                if mi is None:
                    print(f"\n✗ Multiplicative Inverse does NOT exist!")
                    print(f"  Reason: GCD({a}, {m}) ≠ 1")
                    print(f"  (MI only exists if a and m are coprime)")
                else:
                    print(f"\n=== MULTIPLICATIVE INVERSE RESULT ===")
                    print(f"Multiplicative Inverse of {a} mod {m} = {mi}")
                    
                    print(f"\nVerification:")
                    print(f"  ({a} × {mi}) mod {m} = {(a * mi) % m}")
                    print(f"  ✓ Confirmed: {a}×{mi} ≡ 1 (mod {m})")
                    
                    print(f"\nApplications:")
                    print(f"  • RSA: Finding private exponent d")
                    print(f"  • Hill Cipher: Finding matrix inverse")
                    print(f"  • Affine Cipher: Finding multiplicative key inverse")
                    print(f"  • Modular equations: Solving ax ≡ b (mod m)")
            
            except ValueError:
                print("Invalid input! Please enter integers.")
        
        elif choice == '2':
            break
        
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    multiplicative_inverse_menu()
