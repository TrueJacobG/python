t = int(input())


def AreCandiesDivisible(one, two):
    if (one + 2 * two) % 2 != 0:
        return "NO"
    s = (one + 2 * two)//2
    if s % 2 == 0 or s % 2 == 1 and one != 0:
        return "YES"
    return "NO"


for test in range(t):
    n = int(input())
    candies = [int(x) for x in input().split()]
    one = candies.count(1)
    two = candies.count(2)
    print(AreCandiesDivisible(one, two))
