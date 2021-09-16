def drawDiamond(size):
    spaces = size//2
    symbols = 1
    direction = 1
    while spaces < size//2+1:

        print(" " * spaces + "#" * symbols)

        if spaces == 0:
            direction = -1

        spaces -= 1 * direction
        symbols += 2 * direction


def main():
    drawDiamond(10)


if __name__ == '__main__':
    main()
