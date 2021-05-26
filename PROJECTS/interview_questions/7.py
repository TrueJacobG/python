# write only numbers with duplicats
from random import randint

list = [randint(1, 10) for x in range(0, 21)]

print(set([x for x in list if list.count(x) > 1]))
