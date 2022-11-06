from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import os


dir=os.listdir('./data')
# Private RSA key
private_key = RSA.import_key(open('private_key').read())
# Private decrypter
private_crypter = PKCS1_OAEP.new(private_key)

s=""

for i in dir:
    with open("./data/"+i, 'rb') as f:
        enc_fernet_key = f.read()
        # print(enc_fernet_key)
        # print(private_key)
        # Decrypted session key
        dec_fernet_key = private_crypter.decrypt(enc_fernet_key)
        try:
            print(dec_fernet_key.decode())
            s+=dec_fernet_key.decode()
        
        except:
            print("Not valid char")



        with open('/dump/output.txt', 'w') as ff:
            ff.write(s)
        
