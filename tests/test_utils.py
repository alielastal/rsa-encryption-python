import unittest
from rsa_encryption.utils import is_prime, generate_large_prime, generate_rsa_keys

class TestRSAUtils(unittest.TestCase):
    
    def test_is_prime(self):
        # Test some known prime numbers
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(13))
        self.assertTrue(is_prime(17))
        
        # Test some non-prime numbers
        self.assertFalse(is_prime(15))
        self.assertFalse(is_prime(18))
        self.assertFalse(is_prime(21))
    
    def test_generate_large_prime(self):
        # Test that the generated number is prime
        prime = generate_large_prime(bits=8)
        self.assertTrue(is_prime(prime))
    
    def test_generate_rsa_keys(self):
        # Test that keys are generated and that n = p * q
        public_key, private_key = generate_rsa_keys(bits=8)
        n, e = public_key
        p, q = private_key
        
        # Check that n is equal to the product of p and q
        self.assertEqual(n, p * q)
        
        # Check that public and private keys are different
        self.assertNotEqual(public_key, private_key)

if __name__ == '__main__':
    unittest.main()