def countUniqeWords(txt):
    txt = txt.lower().split(" ")
    return len(set(txt))


with open("text1.txt", "r") as f1:
    words = countUniqeWords(f1.read())
    print("PAKO - BANKOMAT: 60 linijki zawierają -> ", words)

print("################################")

with open("text2.txt", "r") as f2:
    words = countUniqeWords(f2.read())
    print("Taco - LUXEMURG: 50 linijki zawierają -> ", words)

print("################################")

with open("text3.txt", "r") as f3:
    words = countUniqeWords(f3.read())
    print("Kaz - Korpotwarze: 44 linijki zawierają -> ", words)
