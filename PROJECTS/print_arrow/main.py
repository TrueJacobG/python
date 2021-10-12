def print_arrow(size, direction="right"):

    changed = False
    symbol = "#"

    if direction == "right" or direction == "left":
        if size % 2 == 0:
            size += 1

        if direction == "right":
            deleter = size//2
            d = -1
        else:
            deleter = 0
            d = 1

        for x in range(size):
            if x <= size//2:
                line = " " * (size//2-deleter-x*d)
            else:
                line = " " * (x*d-size//2*d+deleter)
            for _ in range(size):
                line += symbol
            print(line)
    else:
        if direction == "down":
            step = (size * 2) + 1
            d = -1
            deleter = size
        else:
            step = 1
            d = 1
            deleter = 0

        for x in range(size+1):
            line = " " * (size-deleter - x * d)
            for _ in range(step):
                line += symbol
            print(line)
            step += 2 * d


def main():
    # print_arrow(size=10, direction="down")
    # print_arrow(size=10, direction="up")
    # print_arrow(size=10, direction="right")
    # print_arrow(size=10, direction="left")
    print("DONE")


if __name__ == '__main__':
    main()
