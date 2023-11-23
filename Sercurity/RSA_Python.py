import random
from sympy import mod_inverse


def is_prime(num):
    """Kiểm tra xem một số có phải là số nguyên tố hay không."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def generate_keypair(bits):
    """Tạo cặp khóa (public key, private key)."""
    p = q = 0
    while not is_prime(p):
        p = random.getrandbits(bits)
    while not is_prime(q) or q == p:
        q = random.getrandbits(bits)
    n = p * q
    phi = (p - 1) * (q - 1)

    # Chọn số nguyên tố cùng nhau với phi
    e = random.randint(2, phi - 1)
    while e % phi == 0 or not is_prime(e):
        e = random.randint(2, phi - 1)

    # Tính khóa riêng tư
    d = mod_inverse(e, phi)

    return ((e, n), (d, n))


def encrypt(message, public_key):
    """Mã hóa thông điệp."""
    e, n = public_key
    cipher_text = [pow(ord(char), e, n) for char in message]
    return cipher_text


def decrypt(cipher_text, private_key):
    """Giải mã thông điệp."""
    d, n = private_key
    plain_text = ''.join([chr(pow(char, d, n)) for char in cipher_text])
    return plain_text


# Sử dụng ví dụ
message = "Hello"
public_key, private_key = generate_keypair(bits=8)


ascii_values = [ord(char) for char in message]


print("Public Key: ",public_key)

print("Private Key: ",private_key)

print("ASCII Values:", ascii_values)
# Mã hóa
encrypted_message = encrypt(message, public_key)
print("Encrypted Message:", encrypted_message)

# Giải mã
decrypted_message = decrypt(encrypted_message, private_key)
print("Decrypted Message:", decrypted_message)
