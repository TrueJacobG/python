from random import randint
import time


def main():
    start = time.time()
    arr = [randint(0, 1000000) for _ in range(1000001)]
    arr = sorted(arr)
    print("It takes ", time.time() - start, " seconds")


if __name__ == '__main__':
    main()
