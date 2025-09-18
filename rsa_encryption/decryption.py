class RSADecryption:
    def __init__(self, public_key, private_key):
        self.public_key = public_key
        self.private_key = private_key

    def decrypt(self, ciphertext):
        n, d = self.private_key
        decrypted_text = ''.join([chr(pow(char, d, n)) for char in ciphertext])  # Decrypt each number
        return decrypted_text