def count(number1, number2, symbol):
    if symbol == "*":
        return number1 * number2
    if symbol == "-":
        return number1 - number2
    if symbol == "+":
        return number1 + number2
    if symbol == "/":
        return number1 // number2


def zero(flag=False):
    if flag == False:
        return 0
    return count(0, flag[0], flag[1])


def one(flag=False):
    if flag == False:
        return 1
    return count(1, flag[0], flag[1])


def two(flag=False):
    if flag == False:
        return 2
    return count(2, flag[0], flag[1])


def three(flag=False):
    if flag == False:
        return 3
    return count(3, flag[0], flag[1])


def four(flag=False):
    if flag == False:
        return 4
    return count(4, flag[0], flag[1])


def five(flag=False):
    if flag == False:
        return 5
    return count(5, flag[0], flag[1])


def six(flag=False):
    if flag == False:
        return 6
    return count(6, flag[0], flag[1])


def seven(flag=False):
    if flag == False:
        return 7
    return count(7, flag[0], flag[1])


def eight(flag=False):
    if flag == False:
        return 8
    return count(8, flag[0], flag[1])


def nine(flag=False):
    if flag == False:
        return 9
    return count(9, flag[0], flag[1])


def plus(number):
    return [number, "+"]


def minus(number):
    return [number, "-"]


def times(number):
    return [number, "*"]


def divided_by(number):
    return [number, "/"]


print(seven(times(five())))
print(four(plus(nine())))
print(eight(minus(three())))
print(six(divided_by(two())))
