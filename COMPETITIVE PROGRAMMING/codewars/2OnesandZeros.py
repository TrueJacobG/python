def find_it(seq):
    for number in seq:
        result = seq.count(number)
        if result % 2 != 0:
            return number


print(find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]))
