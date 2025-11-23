def extended_euclidean(a, b):
    """Extended Euclidean Algorithm
    Returns GCD of a and b and shows table steps
    """
    if a > b:
        r1 = a
        r2 = b
    else:
        r1 = b
        r2 = a

    print("\nQ   R1   R2   R")
    print("-" * 25)

    while r2 != 0:
        q = r1 // r2
        r = r1 % r2
        print(q, r1, r2, r)
        r1 = r2
        r2 = r

    return r1


def extended_gcd_menu():
    while True:
        print("\n=== GCD USING EXTENDED EUCLIDEAN ALGORITHM ===")
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

                gcd_val = extended_euclidean(a, b)
                print(f"\nGCD({a}, {b}) = {gcd_val}")

            except ValueError:
                print("Invalid input! Enter integers only.")

        elif choice == '2':
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    extended_gcd_menu()