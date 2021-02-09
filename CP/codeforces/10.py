word = input()
list_word = list(word)
list_word[0] = list_word[0].upper()

result = ""

for i in list_word:
    result += i

print(result)
