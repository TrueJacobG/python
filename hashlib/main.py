import hashlib

code = hashlib.md5()

code.update(b"Hi :D")

print(code.hexdigest())
