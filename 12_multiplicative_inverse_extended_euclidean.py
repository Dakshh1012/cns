"""
Multiplicative Inverse using Extended Euclidean Algorithm
Finds the multiplicative inverse of a number modulo m
Formula: Find MI such that (a × MI) ≡ 1 (mod m)

Mathematical Basis:
If gcd(a, m) = 1, then Extended Euclidean gives us: a*x + m*y = 1
Taking mod m: (a*x) mod m = 1
So x is the multiplicative inverse of a modulo m
"""

def extended_gcd(a, b):
    """Extended Euclidean Algorithm
    Returns: (gcd, x, y) where a*x + b*y = gcd
    """
    if b == 0:
        return a, 1, 0
    else:
        gcd_val, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd_val, x, y

def multiplicative_inverse_extended_euclidean(a, m):
    """Find multiplicative inverse of a mod m using Extended Euclidean
    Returns: MI such that (a * MI) ≡ 1 (mod m)
    
    Steps:
    1. Use Extended Euclidean to find gcd(a, m) and coefficients
    2. If gcd(a, m) ≠ 1, inverse doesn't exist
    3. Otherwise, x from Extended Euclidean is the multiplicative inverse
    4. Return (x mod m + m) mod m to ensure positive result
    """
    gcd_val, x, y = extended_gcd(a, m)
    
    if gcd_val != 1:
        return None, None, None  # Multiplicative inverse doesn't exist
    
    # x is the inverse, normalize to positive
    mi = (x % m + m) % m
    
    return mi, gcd_val, x

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
                
                mi, gcd_val, x = multiplicative_inverse_extended_euclidean(a, m)
                
                if mi is None:
                    print(f"\n✗ Multiplicative Inverse does NOT exist!")
                    print(f"  Reason: GCD({a}, {m}) = {gcd_val} ≠ 1")
                    print(f"  (Inverse only exists if a and m are coprime)")
                else:
                    print(f"\n=== MULTIPLICATIVE INVERSE RESULT ===")
                    print(f"Multiplicative Inverse of {a} mod {m} = {mi}")
                    
                    print(f"\nExtended Euclidean Coefficients:")
                    print(f"  GCD({a}, {m}) = {gcd_val}")
                    print(f"  {a} × {x} + {m} × y = {gcd_val}")
                    
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
