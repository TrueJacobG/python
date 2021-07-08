from multiprocessing import Pool


def doSomething(v):
    for x in range(1000):
        for y in range(1000):
            v += x + y
    return v


if __name__ == '__main__':
    # Pool will do multiprocessing for us, auto-multi
    # automatically divide for max processors
    # func -> map, apply, join, close
    pool = Pool()

    howManyTimes = range(100)
    result = sum(pool.map(doSomething, howManyTimes))

    pool.close()
    pool.join()
    print(result)
