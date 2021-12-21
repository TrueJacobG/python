def hanoi(n, a, b, c):
    if n > 0:
        hanoi(n-1, a, c, b)
        b.append(a.pop())
        hanoi(n-1, c, b, a)


def main():
    a, b, c = ["e", "d", "c", "b", "a"], [], []
    hanoi(5, a, b, c)
    print(a, b, c)


if __name__ == '__main__':
    main()
