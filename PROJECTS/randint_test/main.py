from matplotlib import pyplot as plt
from random import randint

x = []
y = []

growth = 0
fall = 0

for i in range(100):
    x.append(i)
    y.append(randint(1, 10))

for i in range(len(x)-1):
    if y[i] < y[i+1]:
        growth += 1
    elif y[i] > y[i+1]:
        fall += 1
    else:
        pass

print("GROW: ", growth, "FALL: ", fall)

# plt.figure(0)
#plt.plot(x, y)
# plt.show()
