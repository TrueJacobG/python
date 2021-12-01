def main():
    R = 2
    S = 143
    result = 0
    counter = 0
    # 5

    # 1
    # r - 1
    # r(r+1) - 2
    # r(r+1)(r+2)-3

    result += 1 + R - 1

    counter += 2

    if(result > S):
        return counter

    i = 1
    d = 2
    while(result < S):
        counter += 1
        x = 1
        j = 1
        while(j <= i):
            x *= R + j
            j += 1

        result += (R * x) - d
        i += 1
        d += 1

    return counter


if __name__ == '__main__':
    print(main())
