def isequal(l):
    return len(set(l)) <= 1


def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
    l: list[bool] = []
    for c in candies:
        if c + extraCandies > max(candies):
            l.append(True)
        else:
            l.append(False)
    return l


print(kidsWithCandies([2, 3, 5, 1, 3], 3))
