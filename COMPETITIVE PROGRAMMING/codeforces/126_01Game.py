t = int(input())


def makeMove(seq):
    global s, player1, player2, move
    try:
        index = s.index(seq)
    except:
        return False
    s = s[:index] + "" + s[index+2:]
    if move == player1:
        move = player2
    else:
        move = player1
    return True


for _ in range(t):
    s = input()
    player1 = 0
    player2 = 1
    move = player1
    while s:
        isMovePossible = makeMove("01")
        if isMovePossible:
            continue
        else:
            isMovePossible = makeMove("10")
            if isMovePossible:
                continue
            else:
                break

    if move == player2:
        print("DA")
    else:
        print("NET")
