def main():
    t = int(input())

    for test in range(t):
        arr = []
        n = int(input())
        for c in range(n):
            arr.append(1)

        print(" ".join(str(x) for x in arr))


if __name__ == '__main__':
    main()

# 1 1 3 3 7 7 15 15
