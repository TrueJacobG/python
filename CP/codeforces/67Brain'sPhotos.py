t = [int(x) for x in input().split()]
m = t[0]
text = ""

for _ in range(m):
    text += input()

text = text.replace(" ", "")
black_and_white = True

if "C" in text or "M" in text or "Y" in text:
    black_and_white = False

if black_and_white:
    print("#Black&White")
else:
    print("#Color")
