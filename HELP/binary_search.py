from bisect import bisect_left, bisect_right, bisect

l = [2, 4, 8, 6, 7, 8, 9]
#    1  2  5  3  4  6  7
l_sorted = sorted(l)
# l ->  2 4 6 7 8 8 9
# id -> 1 2 3 4 5 6 7
x = 8
# same
print(bisect(l, x))
print(bisect_right(l, x))
# return 6


print(bisect_left(l, x))
# return 5
