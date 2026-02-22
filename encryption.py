from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import base64

def generate_key():
    """
    Generates a random 256-bit key for AES encryption.
    """
    return os.urandom(32)

def encrypt_data(data, key):
    """
    Encrypts data using AES (CFB mode).
    
    :param data: Data to be encrypted (string).
    :param key: Encryption key.
    :return: Encrypted data (base64 encoded).
    """
    iv = os.urandom(16)  # Initialization vector
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(data.encode()) + encryptor.finalize()
    return base64.b64encode(iv + encrypted_data).decode()

def decrypt_data(encrypted_data, key):
    """
    Decrypts encrypted data using AES (CFB mode).
    
    :param encrypted_data: Encrypted data (base64 encoded).
    :param key: Decryption key.
    :return: Decrypted data (string).
    """
    decoded_data = base64.b64decode(encrypted_data)
    iv = decoded_data[:16]  # First 16 bytes are the IV
    encrypted_data = decoded_data[16:]
    
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
    return decrypted_data.decode()
