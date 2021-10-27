from typing import List, Set, Dict
from toimport import toimportfunc


def square(a: List[int], b: int) -> int:
    x = toimportfunc(a[0], b)
    return a[0] * b


def not_square(a: Dict[int, float], b: Dict[int, float]) -> Dict[int, float]:
    for key, value in b.items():
        a[key] += value
    return a
