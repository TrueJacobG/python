import time
import numpy as np


def isPrime(number):
    if number <= 1:
        return False
    ar = np.arange(2, number)
    for i in ar:
        if number % i == 0:
            return False
    return True


def howManyPrimeNumbers(n):
    primes = 1
    for number in range(3, n+1):
        if isPrime(number):
            primes += 1
    return primes


start = time.time()

print(howManyPrimeNumbers(20000))
print(time.time() - start)
