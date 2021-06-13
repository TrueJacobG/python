def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        n2 = n3 = 0
        while n % 2 == 0:
            n /= 2
            n2 += 1
        while n % 3 == 0:
            n /= 3
            n3 += 1
        if n == 1 and n2 <= n3:
            print(n3*2-n2)
            continue
        print(-1)


if __name__ == '__main__':
    main()
