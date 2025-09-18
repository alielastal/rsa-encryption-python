class RSAEncryption:
    def __init__(self, bits=8):
        self.bits = bits
        self.public_key, self.private_key = self.generate_keys()

    def generate_keys(self):
        from .utils import generate_rsa_keys
        return generate_rsa_keys(self.bits)

    def encrypt(self, plaintext):
        n, e = self.public_key
        ciphertext = [pow(ord(char), e, n) for char in plaintext]  # Encrypt each character
        return ciphertext