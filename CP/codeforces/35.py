legs = input().split()

result = 0
elements = []

for element in legs:
    if element in elements:
        result += 1
    else:
        elements.append(element)

print(result)
