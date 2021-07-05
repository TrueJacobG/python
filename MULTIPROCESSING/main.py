from threading import Thread
from os import cpu_count
import time


def test_func(a):
    y = []
    for i in range(a):
        for x in range(a):
            y.append(x*i)


threads = []
num_threads = 10

# create processes
for i in range(num_threads):
    t = Thread(target=test_func, args=(100,))
    threads.append(t)

# start
for t in threads:
    t.start()

# waiting for thread
for t in threads:
    t.join()

print("end")
