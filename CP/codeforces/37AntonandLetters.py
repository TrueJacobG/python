letters = input()
letters = letters[1:len(letters)-1]
letters = letters.split(", ")
results = []
result = 0

for element in letters:
    if element in results:
        continue
    else:
        results.append(element)
        result += 1

if letters == ['']:
    print(0)
else:
    print(result)
