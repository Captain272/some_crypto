import hashlib
 



with open("sensitive.txt","rb") as f:
    f_byte= f.read()
    result = hashlib.sha256(f_byte)
    print(result.hexdigest())
    a=result.hexdigest()

with open("output.txt","rb") as f:
    f_byte= f.read()
    result = hashlib.sha256(f_byte)
    print(result.hexdigest())
    b=result.hexdigest()

if a==b:
    print("Verified")