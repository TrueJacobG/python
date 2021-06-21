from math import fabs


def main():
    n, m = (int(x) for x in input().split())
    l = [int(x) for x in input().split()]

    l = sorted(l)
    counter = 0
    result = 0

    for item in l:
        counter += 1
        if item >= 0:
            break
        if counter > m:
            break
        result += fabs(item)

    print(int(result))


if __name__ == '__main__':
    main()
