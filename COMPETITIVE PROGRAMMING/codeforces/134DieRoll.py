
def main():
    y, w = [int(x) for x in input().split()]

    d = (6 - max(y, w)) + 1
    printInCorrence(d)


def printInCorrence(d):
    div = 6
    if div % d == 0:
        div = div // d
        d = 1

    if div % 2 == 0 and d % 2 == 0:
        div = div // 2
        d = d // 2
    print(f"{d}/{div}")


if __name__ == '__main__':
    main()
