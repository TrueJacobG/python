from random import randint
import timeit

# mergesort vs timsort (built-in)


def createRandomList(number):
    return [randint(0, 100) for _ in range(number)]


def merge(left_list, right_list):
    result = []
    pivotL = 0
    pivotR = 0

    while pivotL < len(left_list) and pivotR < len(right_list):
        if left_list[pivotL] < right_list[pivotR]:
            result.append(left_list[pivotL])
            pivotL += 1
        else:
            result.append(right_list[pivotR])
            pivotR += 1

    if pivotL == len(left_list):
        result.extend(right_list[pivotR:])
    else:
        result.extend(left_list[pivotL:])

    return result


def merge_sort(l):
    if len(l) <= 1:
        return l

    left = merge_sort(l[0:len(l)//2])
    right = merge_sort(l[len(l)//2:])

    return merge(left, right)


print(timeit.timeit(lambda: merge_sort(createRandomList(100)), number=10000))

print(timeit.timeit(lambda: sorted(createRandomList(100)), number=10000))
