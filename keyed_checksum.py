import hmac
import hashlib
 

with open("sensitive.txt","rb") as f:
    f_byte= f.read()
    # result = hashlib.sha256(f_byte,hashlib.md5)
    my_hmac = hmac.new(f_byte,b"pass1", hashlib.md5)
    print(my_hmac.digest())
    a=my_hmac.digest()


with open("output.txt","rb") as f:
    f_byte= f.read()
    # result = hashlib.sha256(f_byte,hashlib.md5)
    my_hmac = hmac.new(f_byte,b"pass1", hashlib.md5)
    print(my_hmac.digest())
    b=my_hmac.digest()

if a==b:
    print("Verified")
else:
    print("Not Verified")