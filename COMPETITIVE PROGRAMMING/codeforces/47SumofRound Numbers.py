t = int(input())


for i in range(t):
    number = int(input())
    power = 1
    result = []
    while number > 0:
        if (number % 10) > 0:
            result.append((number % 10)*power)
        number = number // 10
        power *= 10
    print(len(result))
    print(" ".join(str(x) for x in result))
