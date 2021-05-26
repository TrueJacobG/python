# isDigit

string = "jk5j3bk8m3h1kn8b3bh"

result = ''.join(filter(lambda x: not x.isdigit(), string))

print(result)
