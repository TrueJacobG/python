import random
import string

chars = string.printable
length = 12
password = "".join(random.sample(chars, length))
password = password.replace(" ", "")
print(password)
