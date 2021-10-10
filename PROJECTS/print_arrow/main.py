def print_arrow(size, direction="right"):
    changed = False

    if size % 2 == 0:
        size += 1

    if direction == "right":
        deleter = size//2
        d = -1
    else:
        deleter = 0
        d = 1

    for y in range(size):
        if y <= size//2:
            line = " " * (size//2-deleter-y*d)
        else:
            line = " " * (y*d-size//2*d+deleter)
        for x in range(size):
            line += "#"
        print(line)


"""
4   0
3   1
2   2
1   3
0   4
1   3
2   2
3   1
4   0

"""


def main():
    print_arrow(size=10, direction="right")


if __name__ == '__main__':
    main()
