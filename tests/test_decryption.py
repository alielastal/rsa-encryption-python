import unittest
from rsa_encryption.encryption import RSAEncryption
from rsa_encryption.decryption import RSADecryption

class TestRSADecryption(unittest.TestCase):
    
    def setUp(self):
        # Initialize encryption and decryption objects
        self.rsa = RSAEncryption(bits=8)
        self.rsa_decrypt = RSADecryption(public_key=self.rsa.public_key, private_key=self.rsa.private_key)
    
    def test_decryption(self):
        # Test that the decryption correctly restores the original plaintext
        plaintext = "Hello, RSA!"
        ciphertext = self.rsa.encrypt(plaintext)
        decrypted_text = self.rsa_decrypt.decrypt(ciphertext)
        self.assertEqual(plaintext, decrypted_text)

if __name__ == '__main__':
    unittest.main()