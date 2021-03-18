def median(list):
    list.sort()
    length = len(list)
    if length % 2 == 0:
        return (list[length//2] + list[length//2-1])/2
    else:
        return list[length//2]


print(median([1, 2, 3, 4, 5]))
