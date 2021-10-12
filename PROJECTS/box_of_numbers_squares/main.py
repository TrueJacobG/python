def box(arr):
    print('\n')
    for line in arr:
        print(line)
    print('\n')


def print_box(size):
    arr = []
    for y in range(size):
        line = []
        for x in range(size):
            line.append("#")
        arr.append(line)

    n = 1
    for which in range(size//2+1):
        line = []
        for i in range(which, size-which):
            if arr[which][i] != "#":
                box(arr)
                return

            arr[which][i] = n
            n += 1

        for i in range(1+which, size-which-1):
            if arr[i][size-which-1] != "#":
                box(arr)
                return

            arr[i][size-which-1] = n
            n += 1

        for i in range(size-which-1, -1+which, -1):
            if arr[size-which-1][i] != "#":
                box(arr)
                return

            arr[size-which-1][i] = n
            n += 1

        for i in range(size-which-2, 0+which, -1):
            if arr[i][which] != "#":
                box(arr)
                return

            arr[i][which] = n
            n += 1

    box(arr)
    return


def main():
    pass
    # print_box(7)


if __name__ == '__main__':
    main()
