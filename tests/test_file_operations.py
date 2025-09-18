import unittest
import os
from rsa_encryption.file_operations import save_to_file, read_from_file
from rsa_encryption.encryption import RSAEncryption
from rsa_encryption.decryption import RSADecryption

class TestFileOperations(unittest.TestCase):
    
    def setUp(self):
        # Initialize encryption/decryption objects
        self.rsa = RSAEncryption(bits=8)
        self.rsa_decrypt = RSADecryption(public_key=self.rsa.public_key, private_key=self.rsa.private_key)
        
        # File paths for testing
        self.input_file = 'test_input.txt'
        self.output_file = 'test_output.txt'
    
    def test_save_to_file(self):
        # Test saving text to a file
        text = "This is a test text."
        save_to_file(self.input_file, text)
        with open(self.input_file, 'r') as file:
            saved_text = file.read()
        self.assertEqual(text, saved_text)
    
    def test_read_from_file(self):
        # Test reading text from a file
        text = "This is another test text."
        save_to_file(self.input_file, text)
        read_text = read_from_file(self.input_file)
        self.assertEqual(text, read_text)
    
    def test_encryption_decryption_file_operations(self):
        # Test reading, encrypting, and decrypting files
        text = "Text to encrypt."
        save_to_file(self.input_file, text)
        
        # Encrypt the content of the file
        with open(self.input_file, 'r') as file:
            plaintext = file.read()
        
        ciphertext = self.rsa.encrypt(plaintext)
        
        # Save the encrypted content
        save_to_file(self.output_file, ''.join(map(str, ciphertext)))
        
        # Decrypt the content of the file
        decrypted_text = self.rsa_decrypt.decrypt(ciphertext)
        self.assertEqual(plaintext, decrypted_text)
        
        # Clean up test files
        os.remove(self.input_file)
        os.remove(self.output_file)

if __name__ == '__main__':
    unittest.main()