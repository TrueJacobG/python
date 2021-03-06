def inter(number):

    if number <= 99:
        return 0

    numberstr = list(str(number))

    flag = True
    for n in range(0, len(numberstr)):
        if n != 0:
            if numberstr[n] != '0':
                flag = False

    if flag:
        return 2

    flag = True
    for n in range(0, len(numberstr)-1):
        if numberstr[n] != numberstr[n+1]:
            flag = False
    if flag:
        return 2

    flag = True
    for n in range(0, len(numberstr)-1):
        x = list(str(int(numberstr[n])+1))
        y = list(str(int(numberstr[n+1])))
        if x[len(x)-1] != y[len(y)-1]:
            flag = False
    if flag:
        return 2

    flag = True
    for n in range(0, len(numberstr)-1):
        x = list(str(int(numberstr[n])-1))
        y = list(str(int(numberstr[n+1])))
        if x[len(x)-1] != y[len(y)-1]:
            flag = False
    if flag:
        return 2

    flag = True
    for n in range(0, len(numberstr)-1//2):
        if numberstr[n] != numberstr[len(numberstr)-1-n]:
            flag = False
    if flag:
        return 2

    return 0


def is_interesting(number, awesome_phrases):
    if inter(number) == 0:
        for n in awesome_phrases:
            if n == number:
                return 2
            if number + 1 == n or number + 2 == n:
                return 1
    else:
        return inter(number)
    if inter(number + 1) == 2 or inter(number + 2) == 2:
        return 1


tests = [
    {'n': 100, 'interesting': [1337, 256]}
]
for t in tests:
    print(is_interesting(t['n'], t['interesting']))
