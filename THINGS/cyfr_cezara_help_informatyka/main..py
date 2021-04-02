alf1pl = "AĄBCĆDEĘFGHIJKLŁMNOÓPQRSŚTUWXYZŹŻ"
alf2pl = "RSŚTUWXYZŹŻABCĆDEĘFGHIJKLŁMNOÓPQ"
wordpl = "NIE MA RZECZY ZE WSZYSTKICH STRON SZCZĘŚLIWEJ"

alf1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alf2 = "RSTUVWXYZABCDEFGHIJKLMNOPQ"
word = "NIE MA RZECZY ZE WSZYSTKICH STRON SZCZESLIWEJ"

alf1_no_rep = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alf2_no_rep = "QRSTUVWXYZABCDEFGHIJKLMNOP"
word_no_rep = "NIE MA RZECZY ZE WSZYSTKICH STRON SZCZESLIWEJ"

result = ""

word_no_rep = word_no_rep.replace(" ", "")

for letter in word_no_rep:
    ind = alf1_no_rep.find(letter)
    result += alf2_no_rep[ind]
print(result)
