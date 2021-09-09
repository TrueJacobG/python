from multiprocessing import Process
from time import time
from os import cpu_count


def selfDividingNumbers(left, right):
    result = []
    for number in range(left, right+1):
        divs = [int(x) for x in list(str(number))]
        if 0 in divs:
            continue
        isSelfDividing = 0
        for div in divs:
            if number % div == 0:
                isSelfDividing += 1
        if isSelfDividing == len(divs):
            result.append(number)

    return result


def main():
    starting = time()

    lefts = [x for x in range(0, 10000)]
    rights = [x for x in range(300, 80000)]

    result = []

    for i in range(10000):
        result += selfDividingNumbers(lefts[i], rights[i])

    result = sorted(result)

    print(result[:50])
    print("Done in ", time()-starting)


if __name__ == '__main__':
    # main()
    # 4.81 seconds

    # processes = []
    # cpus = cpu_count()

    # for _ in range(cpus):
    #     p = Process(target=main)
    #     processes.append(p)

    # for p in processes:
    #     p.start()

    # for p in processes:
    #     p.join()
    # sometimes went wrong
