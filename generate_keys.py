from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import base64

# Generates RSA Public and Private keys
key = RSA.generate(3072)

private_key = key.export_key()
with open('private_key', 'wb') as f:
    f.write(private_key)

public_key = key.publickey().export_key()
with open('public_key', 'wb') as f:
    f.write(public_key)