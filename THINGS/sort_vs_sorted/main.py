import time
import random

l1 = []
for x in range(1000000):
    l1.append(random.randint(1, 1000))
l2 = l1

# Sort
time_s1 = time.time()
l1.sort()
print("Sort: "+str(time.time() - time_s1))

# Sorted
time_s2 = time.time()
z = sorted(l2)
print("Sorted: "+str(time.time() - time_s2))

# Sorted is faster than .sort
