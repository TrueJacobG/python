from collections import OrderedDict


def restoreString(s: str, ind: list[int]) -> str:
    d = dict(zip(ind, s))
    d = OrderedDict(sorted(d.items()))
    return "".join(d.values())


print(restoreString("codeleet", [4, 5, 6, 7, 0, 2, 1, 3]))
