def printSquareTimes(number, string):
    for _ in range(giveSquare(number)):
        print(reverseString(string))


def giveSquare(number):
    return number ** 2


def reverseString(string):
    return string[::-1]


printSquareTimes(2, "HI!")
