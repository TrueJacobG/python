import argparse
from linear_function import drawLineFunc
from quadratic_function import drawQuadFunc


def getFloat(x):
    if x != "" and x != "+" and x != "-":
        return float(x)
    else:
        return 0


def getArgs(fnc):
    x1 = fnc.index("x")
    a = fnc[1:x1]

    if fnc.count("x") == 1:
        a = getFloat(a)
        b = getFloat(fnc[x1+1:])

        return 0, a, b

    x2 = fnc.index("x", x1+2)
    b = fnc[x1+2:x2]
    c = fnc[x2+1:]

    a = getFloat(a)
    b = getFloat(b)
    c = getFloat(c)

    return a, b, c


def main():
    parser = argparse.ArgumentParser(
        description="Linear: ax + b for example: =2x+3 \n Quadratic: ax^2+bx+c for example: =2xx+3+1")
    parser.add_argument("func", metavar="func", type=str)

    a, b, c = getArgs(parser.parse_args().func)

    if a == 0:
        drawLineFunc(a, b, -5, 5)
    else:
        drawQuadFunc(a, b, c, -5, 5)


if __name__ == '__main__':
    main()
