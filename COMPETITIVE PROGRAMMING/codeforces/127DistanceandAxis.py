def main():
    x, k = (int(x) for x in input().split())
    if k > x:
        return k-x
    if x % 2 == k % 2:
        return 0
    return 1


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        print(main())
