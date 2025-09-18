import unittest
from rsa_encryption.encryption import RSAEncryption

class TestRSAEncryption(unittest.TestCase):
    
    def setUp(self):
        # Initialize the encryption object with default key size
        self.rsa = RSAEncryption(bits=8)
    
    def test_encryption(self):
        # Test that encryption works by checking if the encrypted text is not equal to the original
        plaintext = "Hello, RSA!"
        ciphertext = self.rsa.encrypt(plaintext)
        self.assertNotEqual(plaintext, ciphertext)
    
    def test_key_generation(self):
        # Test that the public and private keys are generated and are not equal
        public_key, private_key = self.rsa.public_key, self.rsa.private_key
        self.assertNotEqual(public_key, private_key)
    
if __name__ == '__main__':
    unittest.main()