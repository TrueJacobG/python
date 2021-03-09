n = int(input())
word = input()
word = word.lower()
word = sorted(word)

result = ""

for letter in word:
    if letter not in result:
        result += letter

if len(result) == 26:
    print("YES")
else:
    print("NO")
