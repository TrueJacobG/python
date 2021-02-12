# print list in revarse
from random import randint
list = [randint(1, 100) for i in range(0, 11)]


def reverse_list(array):
    copy = []
    for x in range(len(array)-1, -1, -1):
        copy.append(array[x])
    return copy


def rev(list):
    return list[::-1]


print(list)
print(reverse_list(list))
print(rev(list))
