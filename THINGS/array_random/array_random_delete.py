from random import randint

array = [randint(1, 100) for i in range(0, 100)]
print(array)
empty = 0

for i in range(0, 100):
    try:
        array.pop(randint(0, 100))
    except:
        empty += 1

print(array)
print("Empty -> " + str(empty))
