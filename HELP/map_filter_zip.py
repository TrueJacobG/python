def square(a):
    return a**2


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map
print(list(map(square, l)))

# filter -> what you will give for a 1st argument it won't be display
# data = ["", 1, 2, "" , 5]
# print -> filter(None, data) -> [1,2,5]
print(list(filter(lambda x: x > 5, l)))

# zip -> zip two tables
a = [1, 2, 3]
b = [4, 5, 6]
print(list(zip(a, b)))
