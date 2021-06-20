firstLine = "qwertyuiop"
secondLine = "asdfghjkl;"
thirdLine = "zxcvbnm,./"

direction = input()
seq = input()

if direction == "R":
    direction = -1
else:
    direction = 1

result = ""


def addCorrectLetter(i, line):
    global seq, direction, result
    if seq[i] in line:
        index = line.index(seq[i])
        result += line[index+direction]


for i in range(len(seq)):
    addCorrectLetter(i, firstLine)
    addCorrectLetter(i, secondLine)
    addCorrectLetter(i, thirdLine)

print(result)
