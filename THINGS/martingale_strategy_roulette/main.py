from random import randint

# Martingale Strategy Roulette


def gambling(m):
    if randint(0, 1) == 0:
        return -m
    return m*2


def play():
    money = 1000
    value = 1
    throw = 0
    playFlag = True
    while playFlag:
        throw += 1
        money_last_round = money
        money += gambling(value)
        if money_last_round > money:
            if value * 2 > money:
                value = money
            else:
                value *= 2

        if money < 0:
            return 0
        if money >= 2000:
            return 1
        if throw > 100:
            return 0


games = []
n_games = 10000
for p in range(1, n_games):
    games.append(play())

print("WinRatio -> " + str(sum(games)/n_games*100))
