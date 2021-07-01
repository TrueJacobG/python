t = int(input())


def allOddOrEven(a):
    even = 0
    odd = 0
    for number in a:
        if number % 2 == 0:
            even += 1
        else:
            odd += 1
    if even == len(a):
        return True
    if odd == len(a):
        return True
    return False


for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]

    if allOddOrEven(a):
        print("YES")
    else:
        print("NO")
