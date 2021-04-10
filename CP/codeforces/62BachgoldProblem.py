n = int(input())
score = 0
numbers = []
while n != 0:
    if n == 3:
        n -= 3
        score += 1
        numbers.append(3)
        continue
    n -= 2
    score += 1
    numbers.append(2)

print(score)
print(" ".join(str(x) for x in numbers))
