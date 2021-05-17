from random import randint

# Martingale Strategy Roulette


def gambling(m):
    if randint(0, 1) == 0:
        return (-m)
    return m


def play():
    money = 100
    d_money = money*2
    value = 1
    throw = 0
    while True:
        throw += 1
        money_last_round = money
        money += gambling(value)
        if money_last_round > money:
            if value * 2 > money:
                value = money
            else:
                value *= 2
        else:
            value = 1

        if money < 0:
            return 0
        if money >= d_money:
            return 1


games = []
n_games = 100
for p in range(0, n_games):
    games.append(play())

print("You won " + str(sum(games)) + " of " + str(n_games) + " games")
