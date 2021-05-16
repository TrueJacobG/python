import hashlib
from itertools import permutations
import string
import time

password = input("Type hashed password here: ")

start_time = time.time()

list_chars = list(string.printable)
length = 0
test_password = ""


while password != test_password:
    perm = permutations(list_chars, length)
    length += 1
    for p in perm:
        word = "".join(p)
        s_obj = hashlib.md5(word.encode())
        test_password = s_obj.hexdigest()
        print(word + "\033[91m" + " -> " + test_password + "\033[0m")
        if test_password == password:
            break
    else:
        continue
    break

print("Password -> " + "\033[92m" + word + "\033[0m")
print("Time of execution: " +
      "\033[92m" + str(round(time.time() - start_time, 3)) + "\033[0m" + " seconds")
