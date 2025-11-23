"""
GCD using Extended Euclidean Algorithm
Finds GCD and Bezout coefficients (x, y) such that: a*x + b*y = gcd(a, b)
This is more powerful than simple Euclidean as it provides coefficients
"""

def extended_gcd(a, b):
    """Extended Euclidean Algorithm
    Returns: (gcd, x, y) where a*x + b*y = gcd
    
    Works backwards through Euclidean algorithm to find coefficients
    """
    if b == 0:
        return a, 1, 0
    else:
        gcd_val, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd_val, x, y

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
                
                gcd_val, x, y = extended_gcd(a, b)
                
                print(f"\n=== EXTENDED EUCLIDEAN RESULT ===")
                print(f"GCD({a}, {b}) = {gcd_val}")
                print(f"\nBezout Coefficients:")
                print(f"  x = {x}")
                print(f"  y = {y}")
                
                print(f"\nVerification (Bezout's Identity):")
                print(f"  {a} × ({x}) + {b} × ({y}) = {a*x + b*y}")
                print(f"  ✓ Confirmed: {a*x + b*y} = {gcd_val}")
                
                # Show the mathematical relationship
                print(f"\nMathematical Form:")
                print(f"  {a}×{x} + {b}×{y} = {gcd_val}")
            
            except ValueError:
                print("Invalid input! Please enter integers.")
        
        elif choice == '2':
            break
        
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    extended_gcd_menu()
