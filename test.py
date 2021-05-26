import time


def gsum():
    start = time.time()
    s = 0
    for i in range(100000000):
        s += i
    print(time.time()-start)
    return s


if __name__ == '__main__':
    gsum()
