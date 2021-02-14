number = input()
word = list(input())

a, d = 1, 1

for i in word:
    if i == "A":
        a += 1
    if i == "D":
        d += 1

if a > d:
    print("Anton")
elif d > a:
    print("Danik")
else:
    print("Friendship")
