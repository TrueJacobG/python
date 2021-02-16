# search x in array

def search_x(array, x):
    for i in array:
        if i == x:
            return i


print(search_x([1, 3, 5, 3, 7, 5, 8, 0], 1))
