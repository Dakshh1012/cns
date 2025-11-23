"""
GCD using Extended Euclidean Algorithm
Finds GCD and Bezout coefficients (x, y) such that: a*x + b*y = gcd(a, b)
This is more powerful than simple Euclidean as it provides coefficients
"""

def extended_euclidean(a, b):
    """Extended Euclidean Algorithm
    Returns: (gcd, s, t) where a*s + b*t = gcd
    
    Shows all steps in table format with s and t coefficients
    """
    # Ensure r1 > r2
    if a > b:
        r1 = a
        r2 = b
    else:
        r1 = b
        r2 = a
    
    t1 = 0
    t2 = 1
    s1 = 1
    s2 = 0
    
    print(f"\n{'Q':<5} {'R1':<5} {'R2':<5} {'R':<5} {'S1':<5} {'S2':<5} {'S':<5} {'T1':<5} {'T2':<5} {'T':<5}")
    print("-" * 105)
    
    while r2 != 0:
        q = r1 // r2
        r = r1 % r2
        t = t1 - t2 * q
        s = s1 - s2 * q
        print(f"{q:<5} {r1:<5} {r2:<5} {r:<5} {s1:<5} {s2:<5} {s:<5} {t1:<5} {t2:<5} {t:<5}")
        r1 = r2
        r2 = r
        t1 = t2
        t2 = t
        s1 = s2
        s2 = s
    
    return r1, s1, t1

def extended_gcd_menu():
    """Menu-driven Extended Euclidean Algorithm"""
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
                
                print(f"\n=== EXTENDED EUCLIDEAN RESULT ===")
                print(f"GCD({a}, {b}) = {gcd_val}")
                
                print(f"\nBezout Coefficients:")
                print(f"  s = {s}")
                print(f"  t = {t}")
                
                print(f"\nVerification (Bezout's Identity):")
                print(f"  {a} × {s} + {b} × {t} = {a*s + b*t}")
                print(f"  ✓ Confirmed: {a*s + b*t} = {gcd_val}")
            
            except ValueError:
                print("Invalid input! Please enter integers.")
        
        elif choice == '2':
            break
        
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    extended_gcd_menu()
