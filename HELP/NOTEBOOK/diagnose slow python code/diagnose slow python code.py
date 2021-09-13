import cProfile
import pstats
import time


def f():
    # time.sleep(1)
    for i in range(0, 100):
        for j in range(0, 100):
            x = i + j


def main():
    with cProfile.Profile() as prof:
        f()

    stats = pstats.Stats(prof)
    stats.sort_stats(pstats.SortKey.TIME)
    # stats.print_stats()
    stats.dump_stats(filename="statistics.prof")


if __name__ == "__main__":
    main()
