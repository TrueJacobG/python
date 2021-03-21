word = input()

word_list = list(word)

alpD = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpM = "abcdefghijklmnopqrstuvwxyz"

resD = 0
resM = 0

for i in range(0, len(word_list)):
    if word_list[i] in alpD:
        resD += 1

    if word_list[i] in alpM:
        resM += 1

if resD > resM:
    print(word.upper())
else:
    print(word.lower())
