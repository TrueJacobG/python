import math


def isPP(n):
    now = 2
    maxi = math.floor(n/2)
    while maxi >= now:
        power = 2
        while math.pow(now, power) <= n:
            if math.pow(now, power) == n:
                return [now, power]
            else:
                power += 1
        now += 1
    return None


print(isPP(8))
