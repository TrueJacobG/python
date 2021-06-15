t = int(input())

alphabet = "abcdefghijklmnopqrstuvwxyz"

for _ in range(t):
    n, a, b = [int(x) for x in input().split()]
    result = ""
    id_letter = 0
    while n:
        n -= 1
        result += alphabet[id_letter]
        id_letter += 1
        if id_letter == b:
            id_letter = 0
    print(result)
