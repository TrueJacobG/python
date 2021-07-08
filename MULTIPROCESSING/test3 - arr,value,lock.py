from multiprocessing import Process, Array, Value, Lock
from os import cpu_count


def doSomethingValue(v, lock):
    for x in range(100):
        for y in range(100):
            # when value,arr etc. is lock then other process cannot use this value
            with lock:
                v.value += x + y


def doSomethingArr(arr, lock):
    for x in range(100):
        for y in range(100):
            with lock:
                for i in range(len(arr)):
                    arr[i] += x + y


if __name__ == '__main__':
    cpus = cpu_count()
    processes = []
    lock = Lock()

    # type, value
    val = Value("i", 0)
    # print("#start ", val.value)

    # type, values  -> d == double
    arr = Array("d", [0, 1, 2, 3])
    print("#start ", arr[0])

    for _ in range(cpus):
        p = Process(target=doSomethingArr, args=(arr, lock))
        processes.append(p)

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    # without Lock the value is wrong
    # if you have to do something 1000 you can do it for example 250 with 4 cores -> 4x faster. It's kinda cool :D
    # print("#end ", val.value)

    print("#end", arr[0])
