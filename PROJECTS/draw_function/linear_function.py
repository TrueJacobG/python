import numpy as np
import matplotlib.pyplot as plt
import argparse


def drawLinearFunction(a: int, b: int, start: int, end: int):
    x = np.array(np.arange(start, end+1))
    y = a * x + b
    print(y)
    plt.plot(x, y)
    plt.show()


def getAB(fnc):
    x = fnc.index("x")
    a = fnc[1:x]
    b = fnc[x+1:]
    if a != "":
        a = float(a)
    else:
        a = 0

    if b != "":
        b = float(b)
    else:
        b = 0

    return a, b


def main():
    parser = argparse.ArgumentParser(
        description="PASTE ax + b for example: =2x+3")
    parser.add_argument("func", metavar="func", type=str)
    args = parser.parse_args()

    a, b = getAB(args.func)
    drawLinearFunction(a, b, -5, 5)


if __name__ == '__main__':
    main()
