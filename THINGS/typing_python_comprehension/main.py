from time import time


def Fibonacci(n):
    result = []
    for z in range(0, n):
        if z == 0 or z == 1:
            result.append(z)
        else:
            result.append(sum(result[z-2:z]))
    return result


def typed_Fibonacci(n: int) -> list:
    result: list = []
    for z in range(n):
        if z == 0 or z == 1:
            result.append(z)
        else:
            result.append(sum(result[z-2:z]))
    return result


start1 = time()
Fibonacci(10000)
print(str(time()-start1))

start1 = time()
typed_Fibonacci(10000)
print(str(time()-start1))
