from typing import List


def square(a: int, b: int) -> int:
    return a * b


def not_square(a: List[int], b: List[int]) -> List[int]:
    l = []
    for i in range(len(a)):
        l.append(a[i]+b[i])
    return l
