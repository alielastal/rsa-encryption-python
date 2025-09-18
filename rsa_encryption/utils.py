import random
from math import gcd

# Utility to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Generate a large prime number (for simplicity, this is a basic implementation)
def generate_large_prime(bits=8):
    while True:
        num = random.getrandbits(bits)  # Generate a random number of 'bits' length
        if is_prime(num):
            return num

# Extended Euclidean Algorithm to compute modular inverse
def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

# RSA key generation
def generate_rsa_keys(bits=8):
    p = generate_large_prime(bits)
    q = generate_large_prime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)

    # Find e such that gcd(e, phi) = 1
    e = 65537  # Common choice for e
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    # Find d such that d * e ≡ 1 (mod phi)
    d = modinv(e, phi)
    
    return (n, e), (n, d)  # Return public (n, e) and private (n, d)