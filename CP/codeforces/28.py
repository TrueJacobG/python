n = input()
difficulty = list(input().split())

result = "EASY"

for i in difficulty:
    if i == "1":
        result = "HARD"

print(result)
