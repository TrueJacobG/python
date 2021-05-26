import random
import string

# 16.05.2021

chars = string.printable
length = 12
password = "".join(random.sample(chars, length))
password = password.replace(" ", "")
print(password)
