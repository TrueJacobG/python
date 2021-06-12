def returnBetterPermutations(arr, length):
    result = []
    starting = 0
    ending = length
    while ending <= len(arr):
        result.append(arr[starting:ending])
        starting += 1
        ending += 1
    return result


print(returnBetterPermutations([1, 4, 2, 5, 3], 3))
