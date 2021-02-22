n = int(input())

string = ""

for i in range(1, n+1):
    if i % 2 != 0:
        string += "I hate it "
    else:
        string += "I love it "

string = string.replace("it", "that")

length = len(string)

string = string[:length-5] + "it" + string[length+1:]

print(string)
