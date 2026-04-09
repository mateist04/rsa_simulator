import random
import math

# Greatest common divisor
def gcd(a, b):
    while b != 0:
        a, b = b, a % b # at the end, a will store the gcd
    return a

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0: return False
    return True

def generate_prime(min_val, max_val):
    prime = random.randint(min_val, max_val)

    while is_prime(prime) == False:
        prime = random.randint(min_val, max_val)
    return prime


def modular_inverse(e, phi):
    # t tracks the coefficient 'x' (the future inverse)
    t, t_new = 0, 1

    # r tracks the reminder to find the gcd
    r, r_new = phi, e

    while r_new != 0:
        quotient = r // r_new

        t, t_new = t_new, t - quotient * t_new
        r, r_new = r_new, r - quotient * r_new

    # if the final non-zero remainder is > 1, phi and e aren't coprime
    if r > 1:
        raise Exception("e and phi are not coprime; inverse doesn't exist")
    
    # if the resulting inverse is negative, it needs to be wrapped into the positive modular space
    if t < 0:
        t = t + phi

    return t

def generate_keyPair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("both numbers must be prime!")
    elif p == q:
        raise ValueError("p and q can not be equal")
    
    # calculate n and phi
    n = p * q
    phi = (p - 1) * (q - 1)

    # generate e, so that it doesn't have any common divisors with phi
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    
    # employ the Extended Euclid Algorithm to find the private key
    d = modular_inverse(e, phi)

    # return the public key and private key pairs
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    key, n = pk

    ciphertext = []
    for char in plaintext:
        m = ord(char)
        c = pow(m, key, n)
        ciphertext.append(c)

    return ciphertext

def decrypt(pk, ciphertext):
    key, n = pk
    
    plaintext = []
    for c in ciphertext:
        m = chr(pow(c, key, n))
        plaintext.append(m)

    return ''.join(plaintext)

if __name__ == '__main__':
    print("RSA Cryptography Simulator")

    p = generate_prime(32768, 65535)
    q = generate_prime(32768, 65535)

    while p == q:
        q = generate_prime(32768, 65535)
    
    print(f"Generated primes are: p={p}, q={q}")
    
    public, private = generate_keyPair(p, q)

    print(f"Public key (e, n): {public}")
    print(f"Private key (d, n): {private}")

    message = "This is a confidential message!"
    print(f"\nOriginal Message: '{message}'")
    
    encrypted_msg = encrypt(public, message)
    print(f"This is the encrypted message: '{encrypted_msg}'")

    decrypted_msg = decrypt(private, encrypted_msg)
    print(f"This is the decrypted message: '{decrypted_msg}'")
