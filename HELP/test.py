def largestAltitude(gain):
    actual = 0
    maximum = 0
    helper = []
    for i in range(len(gain)):
        helper.append(actual)
        actual = actual + gain[i]
        maximum = max(maximum, actual)
        print(maximum)
    # print(helper)
    return maximum


print(largestAltitude([-4, -3, -2, -1, 4, 3, 2]))
