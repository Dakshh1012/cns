"""
GCD using Euclidean Algorithm
Finds the greatest common divisor of two numbers
Uses the principle: gcd(a, b) = gcd(b, a mod b)
"""

def euclidean(a, b):
    """Find GCD using Euclidean algorithm
    Returns: gcd(a, b)
    Shows all steps in table format
    """
    # Ensure r1 > r2
    if a > b:
        r1 = a
        r2 = b
    else:
        r1 = b
        r2 = a
    
    steps = []
    print(f"\n{'Q':<5} {'R1':<5} {'R2':<5} {'R':<5}")
    print("-" * 25)
    
    while r2 != 0:
        q = r1 // r2
        r = r1 % r2
        print(f"{q:<5} {r1:<5} {r2:<5} {r:<5}")
        steps.append((q, r1, r2, r))
        r1 = r2
        r2 = r
    
    return r1, steps

def gcd_euclidean_menu():
    """Menu-driven GCD Euclidean algorithm"""
    while True:
        print("\n=== GCD USING EUCLIDEAN ALGORITHM ===")
        print("1. Find GCD")
        print("2. Exit")
        
        choice = input("Enter choice (1-2): ").strip()
        
        if choice == '1':
            try:
                a = int(input("Enter first number (a): ").strip())
                b = int(input("Enter second number (b): ").strip())
                
                if a < 0 or b < 0:
                    print("Please enter positive numbers!")
                    continue
                
                gcd_val, steps = euclidean(a, b)
                
                print(f"\n✓ GCD({a}, {b}) = {gcd_val}")
            
            except ValueError:
                print("Invalid input! Please enter integers.")
        
        elif choice == '2':
            break
        
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    gcd_euclidean_menu()
