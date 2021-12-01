from typing import List, Set, Dict, Tuple
from toimport import toimportfunc


def square(a: Tuple[float], b: int) -> str:
    return str(b)


def not_square(a: Dict[int, float], b: Dict[int, float]) -> Dict[int, float]:
    for key, value in b.items():
        a[key] += value
    return a
