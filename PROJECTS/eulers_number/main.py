from math import factorial
import time
import numpy as np


def eulers_number(n):
    l = [1/factorial(x) for x in range(n)]
    return sum(l)


def eulers_number2(n):
    s = 0
    for x in range(n):
        s += 1/factorial(x)
    return s


def eulers_number3(n):
    arr = [1/factorial(x) for x in range(n)]
    return np.sum(arr)


number = 100

start_time = time.time()
print(eulers_number(number))
print("1st time -> " + str(time.time()-start_time) + " seconds")

start_time = time.time()
print(eulers_number2(number))
print("2st time -> " + str(time.time()-start_time) + " seconds")

start_time = time.time()
print(eulers_number3(number))
print("3st time -> " + str(time.time()-start_time) + " seconds")
