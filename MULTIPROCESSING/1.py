from multiprocessing import Process
from os import cpu_count


def test(n):
    for x in range(n):
        for y in range(n):
            x, y = y, x


def main():
    test(1000)

# You need __name__ to work multiprocessing
if __name__ == '__main__':
    processes = []
    cpus = cpu_count()
    for _ in range(cpus):
        p = Process(target=main)
        processes.append(p)
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    print("Done")
