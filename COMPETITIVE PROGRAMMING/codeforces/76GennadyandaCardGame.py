fcard = input()
hand = input().split()


def main(fcard, hand):
    for card in hand:
        if card[0] == fcard[0]:
            return "YES"
        if card[1] == fcard[1]:
            return "YES"
    return "NO"


print(main(fcard, hand))
