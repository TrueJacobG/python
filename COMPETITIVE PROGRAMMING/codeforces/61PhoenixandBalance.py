t = int(input())

elements = [2**e for e in range(1, 31)]

for _ in range(t):
    power = int(input())
    x = 2**power
    y = 0
    div = power//2
    for i in range(1, power):
        if i < div:
            x += 2**i
        else:
            y += 2**i
    print(x-y)
