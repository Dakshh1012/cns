"""
GCD using Euclidean Algorithm
Finds the greatest common divisor of two numbers
Uses the principle: gcd(a, b) = gcd(b, a mod b)
"""

def gcd_euclidean(a, b):
    """Find GCD using Euclidean algorithm
    Returns: gcd(a, b)
    Shows all steps
    """
    steps = []
    original_a, original_b = a, b
    
    while b != 0:
        q = a // b
        r = a % b
        steps.append(f"{a} = {b} × {q} + {r}")
        a, b = b, r
    
    return a, steps

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
                
                gcd_val, steps = gcd_euclidean(a, b)
                
                print(f"\n=== EUCLIDEAN ALGORITHM STEPS ===")
                for step in steps:
                    print(f"  {step}")
                
                print(f"\n✓ GCD({a}, {b}) = {gcd_val}")
            
            except ValueError:
                print("Invalid input! Please enter integers.")
        
        elif choice == '2':
            break
        
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    gcd_euclidean_menu()
