# RSA Text Encryption and Decryption (Pure Python)

This is a simple Python implementation of the RSA encryption and decryption algorithm. The app allows you to:
- Encrypt and decrypt text using RSA keys.
- Generate RSA keys (public and private).
- Encrypt and decrypt files.

This project uses a **pure Python implementation** of RSA. 

---

## Features
- Generate RSA keys (public and private).
- Encrypt text or text files.
- Decrypt encrypted text or text files.

---

## Getting Started

### Prerequisites
You need to have **Python 3.x** installed.

### Installation
Clone the repository to your local machine:
```bash
git clone https://github.com/your-username/rsa-encryption-streamlit.git
```

### Install dependencies:
``` bash
pip install -r requirements.txt
```

## Usage
``` bash
streamlit run app.py
```

## How it Works

1. **RSA Key Generation**: Generates a public and private key pair. The public key can be used to encrypt data, and the private key is used for decryption.

2. **Encryption**: Input text or upload a .txt file to encrypt using the public key.

3. **Decryption**: Use the private key to decrypt the encrypted text.

## Contributing
1. Fork the repository.

2. Create a new branch (git checkout -b feature-name).

3. Make changes and commit them (git commit -m 'Add new feature').

4. Push to the branch (git push origin feature-name).

5. Open a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.