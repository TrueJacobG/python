from math import fabs

n = int(input())


def findDivider(a, b):
    x = a % b
    if x == 0:
        return 0
    return int(fabs(x - b))


results = []

for _ in range(0, n):
    numbers = input().split(" ")
    a = int(numbers[0])
    b = int(numbers[1])
    results.append(findDivider(a, b))

for item in results:
    print(item)
