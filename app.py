import streamlit as st
from rsa_encryption.encryption import RSAEncryption
from rsa_encryption.decryption import RSADecryption
import io

# Streamlit page config
st.set_page_config(page_title="RSA Encryption App", layout="centered")

st.title("🔐 RSA Text Encryption and Decryption (Pure Python)")
st.markdown("This demo uses a basic pure Python implementation of the RSA algorithm.")

# Text Input Section
st.header("1. 🔤 Enter or Upload Text")

# Option to upload file
uploaded_file = st.file_uploader("Upload a .txt file", type=["txt"])
input_text = ""

if uploaded_file:
    # Read uploaded file content
    stringio = io.StringIO(uploaded_file.getvalue().decode("utf-8"))
    input_text = stringio.read()
else:
    # Manual text entry
    input_text = st.text_area("Or type/paste your text here:", height=150)

if input_text:
    st.success("Text loaded successfully.")
    st.write("**Input Text Preview:**")
    st.code(input_text[:300] + ("..." if len(input_text) > 300 else ""), language="text")
else:
    st.info("Please upload a file or enter text above to continue.")

# RSA Key Generation Section
st.header("2. 🔑 Generate RSA Keys")

# Key generation button
if st.button("Generate RSA Keys"):
    rsa = RSAEncryption(bits=8)  # You can increase the key size (e.g., 1024 or 2048 bits)
    public_key, private_key = rsa.public_key, rsa.private_key
    n, e = public_key
    p, q = private_key

    # Display public and private keys (showing n, e, and d values)
    st.subheader("Public Key (n, e):")
    st.write(f"n: {n}\ne: {e}")

    st.subheader("Private Key (n, d):")
    st.write(f"n: {n}\nd: {p * q}")  # Showing n and d (p * q is used here)

    # Store keys for encryption/decryption
    st.session_state.rsa = rsa  # Store RSA object in session state for later use

# Encryption Section
if 'rsa' in st.session_state:
    st.header("3. ✨ Encrypt the Text")

    # Button to encrypt
    if st.button("Encrypt Text"):
        rsa = st.session_state.rsa
        ciphertext = rsa.encrypt(input_text)
        st.session_state.ciphertext = ciphertext  # Store ciphertext in session state (list of integers)
        st.subheader("Encrypted Text:")
        st.code(' '.join(map(str, ciphertext)))  # Show the encrypted text as a space-separated string of numbers

# Decryption Section
if 'rsa' in st.session_state and 'ciphertext' in st.session_state:
    st.header("4. 🔓 Decrypt the Encrypted Text")

    # Button to decrypt
    if st.button("Decrypt Text"):
        rsa = st.session_state.rsa
        rsa_decrypt = RSADecryption(public_key=rsa.public_key, private_key=rsa.private_key)
        decrypted_text = rsa_decrypt.decrypt(st.session_state.ciphertext)  # Pass the list of integers directly
        st.subheader("Decrypted Text:")
        st.write(decrypted_text)