from random import randrange


def removeAboveUnderMean(l, number, a_or_u):
    l = sorted(l)
    index = l.index(number)

    # 0 -> remove numbers under number
    if a_or_u == 0:
        return l[index:]
    return l[:index+1]


# list of random numbers
l = [randrange(1, 100) for i in range(101)]
print(removeAboveUnderMean(l, 20, 1))
