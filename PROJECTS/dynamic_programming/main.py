import time


def findInFibWithMemo(n):
    if n == 1 and n == 2:
        return 1
    b = [None] * (n+1)
    b[1] = 1
    b[2] = 1
    for i in range(3, n+1):
        b[i] = b[i-1] + b[i-2]
    return b[n]


def findInFib(n):
    if n == 1 or n == 2:
        result = 1
    else:
        result = findInFib(n-1)+findInFib(n-2)
    return result


# DP
# 1000 -> 0.003sec
start = time.time()
print(findInFibWithMemo(1000))
print("DP -> time: ", str(time.time() - start))

# without DP
# 40 -> 30 seconds
# start = time.time()
# findInFib(40)
# print("Without DP -> time: ", str(time.time() - start))
