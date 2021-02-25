def is_valid_walk(walk):
    length = len(walk)
    if length != 10:
        return False
    x = 0
    y = 0
    for i in range(0, length):
        if walk[i] == "n":
            y += 1
        if walk[i] == "s":
            y -= 1
        if walk[i] == "w":
            x -= 1
        if walk[i] == "e":
            x += 1

    if x == 0 and y == 0:
        return True
    else:
        return False


print(is_valid_walk(['s', 'e', 'w', 'n', 'n', 's', 'e', 'w', 'n', 's']))
print(is_valid_walk(['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']))
