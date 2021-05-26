
t = int(input())
numbers = []
for _ in range(t):
    numbers.append(input().split(" "))

for number in numbers:
    a = int(number[0])
    b = int(number[1])
    diff = abs(b - a)
    steps = diff//10
    if a < b:
        if steps * 10 + a != b:
            steps += 1
    else:
        if steps * 10 + b != a:
            steps += 1
    print(steps)
