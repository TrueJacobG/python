
def main():
    k = int(input())
    a = [int(x) for x in input().split()]
    if sum(a) < k:
        return -1

    a = sorted(a, reverse=True)

    result = 0
    plant = 0

    while plant < k:
        result += 1
        plant += a[0]
        del a[0]
    return result


if __name__ == '__main__':
    print(main())
