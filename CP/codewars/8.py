def dig_pow(n, p):
    listN = list(str(n))
    result = 0
    for i in listN:
        result += int(i)**p
        p += 1
    if result % n == 0:
        return result//n
    else:
        return -1


print(dig_pow(89, 1))  # 1
print(dig_pow(92, 1))  # -1
print(dig_pow(46288, 3))  # 51
