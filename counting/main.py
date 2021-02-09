import datetime


def silnia(n):
    if(n == 1):
        return 1
    else:
        return n * silnia(n-1)


start = datetime.datetime.now()

print(silnia(100))
i = 1
while (i < 10000):
    print(i)
    i += 1

stop = datetime.datetime.now() - start

print(stop)
