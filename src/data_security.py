```python
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

class DataSecurity:

    def __init__(self, password_provided):
        password = password_provided.encode()
        salt = b'salt_'
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        self.key = base64.urlsafe_b64encode(kdf.derive(password))

    def encrypt_message(self, message):
        f = Fernet(self.key)
        encrypted = f.encrypt(message)
        return encrypted

    def decrypt_message(self, encrypted_message):
        f = Fernet(self.key)
        decrypted = f.decrypt(encrypted_message)
        return decrypted
```
This python script provides a class `DataSecurity` that can be used to encrypt and decrypt data. It uses a password-based key derivation function to generate a secret key for the Fernet symmetric encryption scheme. The `encrypt_message` and `decrypt_message` methods can be used to encrypt and decrypt messages respectively.