x = int(input())

n = True
result = 1

while n:
    if x <= 5:
        n = False
    else:
        x -= 5
        result += 1

print(result)
