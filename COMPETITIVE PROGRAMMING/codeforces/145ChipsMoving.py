n = int(input())

cords = [int(x) for x in input().split()]
cords = cords

coins = 0

for cord in cords:
    coins += cord & 1

print(min(coins, n - coins))
