from math import fabs


def minDistance(n1, n2):
    change = {6: 4, 7: 3, 8: 2, 9: 1}
    distance = int(fabs(int(n1) - int(n2)))
    if distance <= 5:
        return distance
    return change[distance]


def main():
    n = int(input())
    locked = input()
    unlocked = input()

    result = 0
    for i in range(n):
        result += minDistance(locked[i], unlocked[i])

    print(result)


if __name__ == '__main__':
    main()
