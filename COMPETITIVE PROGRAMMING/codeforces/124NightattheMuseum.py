from math import fabs

word = input()

alpha = "abcdefghijklmnopqrstuvwxyz"
startingPointer = 0
result = 0


def findDistance(letter):
    global alpha, startingPointer
    leftDistance = rightDistance = 0
    current = alpha[startingPointer]
    balance = 26
    # right
    while current != letter:
        rightDistance += 1
        if startingPointer + rightDistance < len(alpha):
            current = alpha[startingPointer + rightDistance]
            continue
        current = alpha[startingPointer + rightDistance - balance]

    current = alpha[startingPointer]
    # left
    while current != letter:
        leftDistance += 1
        if startingPointer - leftDistance > -1:
            current = alpha[startingPointer - leftDistance]
            continue
        current = alpha[startingPointer - leftDistance + balance]

    return (leftDistance, rightDistance)


for letter in word:
    result += min(findDistance(letter))
    startingPointer = alpha.index(letter)

print(result)
