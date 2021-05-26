
text = input()

list = text.split('+')
list.sort()

result = ""

for i in list:
    result += f"{i}+"

result = result[0:len(result)-1]

print(result)
