

def sumoflist(lista):
    suma = 0
    for number in lista:
        suma += int(number)
    return suma


def power_sumDigTerm(n):
    result = []
    for i in range(2, 100):
        for j in range(2, 100):
            iToThePowerOfJ = i ** j
            if sumoflist(list(str(iToThePowerOfJ))) == i:
                result.append(iToThePowerOfJ)
    result = sorted(result)
    return result[n-1]


print(power_sumDigTerm(1))  # 81
print(power_sumDigTerm(2))  # 512
print(power_sumDigTerm(3))  # 2401
print(power_sumDigTerm(4))  # 4913
print(power_sumDigTerm(5))  # 5832
