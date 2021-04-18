t = int(input())

for number in range(t):
    numbers = [int(x) for x in input().split()]
    n = int(numbers[3])
    l = numbers[:3]
    l.sort()
    n -= (2 * int(l[2])) - int(l[1]) - int(l[0])
    if n % 3 == 0 and n >= 0:
        print("YES")
    else:
        print("NO")
