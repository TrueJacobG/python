
def twins(n, coins):
    coins.sort()
    half_sum = sum(coins)//2
    sum2 = 0
    result = 0
    for c in range(n-1, -1, -1):
        sum2 += coins[c]
        result += 1
        if sum2 > half_sum:
            break

    return result


n = int(input())
coins = [int(x) for x in input().split()]

print(twins(n, coins))
