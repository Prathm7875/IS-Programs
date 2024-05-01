import random

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes():
    p = random.randint(100, 1000)
    while not is_prime(p):
        p = random.randint(100, 1000)
    q = random.randint(100, 1000)
    while not is_prime(q) or p == q:
        q = random.randint(100, 1000)
    return p, q

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def generate_keys():
    p, q = generate_primes()
    n = p * q
    phi_n = lcm(p - 1, q - 1)
    e = random.randint(2, phi_n - 1)
    while gcd(e, phi_n) != 1:
        e = random.randint(2, phi_n - 1)
    d = pow(e, -1, phi_n)
    return (e, n), (d, n)

def encrypt(message, public_key):
    e, n = public_key
    return pow(message, e, n)

def decrypt(ciphertext, private_key):
    d, n = private_key
    return pow(ciphertext, d, n)

# Example usage
public_key, private_key = generate_keys()
message = 123
ciphertext = encrypt(message, public_key)
plaintext = decrypt(ciphertext, private_key)
print(f"Public key: {public_key}")
print(f"Private key: {private_key}")
print(f"Message: {message}")
print(f"Ciphertext: {ciphertext}")
print(f"Plaintext: {plaintext}")

# -----------------------------------------------------------------------------------------------------------------

# Output:

# Public key: (52189, 239651)
# Private key: (22213, 239651)
# Message: 123
# Ciphertext: 233934
# Plaintext: 123

