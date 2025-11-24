# HARD-CODED ECC (secp256k1) WITH FULL STEP PRINTING

# Curve parameters (secp256k1)
a = 0
b = 7
p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141

# Generator/Base point G
Gx = 55066263022277343669578718895168534326250603453777594175500187360389116729240
Gy = 32670510020758816978083085130507043184471273380659243275938904335757337482424
G = (Gx, Gy)


def is_on_curve(x, y, a, b, p):
    return (y * y - (x * x * x + a * x + b)) % p == 0


def point_add(P, Q, a, p):
    print("\n--- Point Addition Step ---")
    print(f"P = {P}")
    print(f"Q = {Q}")

    if P is None:
        print("P is infinity → returning Q")
        return Q
    if Q is None:
        print("Q is infinity → returning P")
        return P

    x1, y1 = P
    x2, y2 = Q

    if x1 == x2 and (y1 + y2) % p == 0:
        print("P + Q = Infinity (points cancel out)")
        return None

    s = ((y2 - y1) * pow(x2 - x1, -1, p)) % p
    print(f"slope s = {s}")

    xr = (s * s - x1 - x2) % p
    yr = (s * (x1 - xr) - y1) % p

    print(f"xr = {xr}")
    print(f"yr = {yr}")

    return (xr, yr)


def point_double(P, a, p):
    print("\n--- Point Doubling Step ---")
    print(f"P = {P}")

    if P is None:
        print("Doubling infinity gives infinity")
        return None

    x1, y1 = P

    if y1 == 0:
        print("y1 = 0 → infinity")
        return None

    s = ((3 * x1 * x1 + a) * pow(2 * y1, -1, p)) % p
    print(f"slope s = {s}")

    xr = (s * s - 2 * x1) % p
    yr = (s * (x1 - xr) - y1) % p

    print(f"xr = {xr}")
    print(f"yr = {yr}")

    return (xr, yr)


def scalar_mul(k, P, a, p):
    print("\n============================")
    print(f"Scalar Multiplication: {k} * P")
    print("============================")

    result = None
    add_point = P
    bit_index = 0

    while k > 0:
        print(f"\nBit {bit_index}: k = {k}, last bit = {k & 1}")

        if k & 1:
            print("→ Adding add_point to result")
            result = point_add(result, add_point, a, p)
            print(f"Result now = {result}")

        print("→ Doubling add_point")
        add_point = point_double(add_point, a, p)
        print(f"add_point after doubling = {add_point}")

        k >>= 1
        bit_index += 1

    print("\nFINAL RESULT =", result)
    return result


# -------------------- MAIN EXECUTION --------------------

print("=== HARD-CODED ECC (secp256k1) ===")

# Check G is valid point
print("\nChecking base point G...")
if is_on_curve(Gx, Gy, a, b, p):
    print("✔ G lies on the elliptic curve")
else:
    print("✘ ERROR: G is not on the curve!")
    exit()

# Hardcode private key
private_key = 13   # you can change this anytime
print(f"\nPrivate key k = {private_key}")

# Compute public key
public_key = scalar_mul(private_key, G, a, p)

print("\n============================")
print("PUBLIC KEY:")
print(public_key)
print("============================")
