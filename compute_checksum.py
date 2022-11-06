import hashlib
 

with open("sensitive.txt","rb") as f:
    f_byte= f.read()
    result = hashlib.sha256(f_byte)
    print(result.hexdigest())