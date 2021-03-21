n = input()
n2 = input()

result = ""

for i in range(len(n)):
    if n[i] == n2[i]:
        result += '0'
    else:
        result += '1'

print(result)
