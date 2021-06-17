from random import randrange


def binarySearch(data: list[int], number: int) -> int:
    left: int = 0
    right: int = len(data)-1
    mid: int = 0
    while left <= right:
        mid = left + (right - left)//2
        if data[mid] == number:
            return mid
        if number > data[mid]:
            left = mid + 1
        if number < data[mid]:
            right = mid - 1
    return -1


def main():
    l: list[int] = sorted([randrange(1, 10) for x in range(1, 10)])
    print(l)
    print(binarySearch(l, 8))


if __name__ == '__main__':
    main()
