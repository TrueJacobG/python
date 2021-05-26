money = 10000
daily_interest = 0.01
days = 3

while(days != 0):
    money = money + (money * daily_interest)
    days -= 1

print(int(money))
