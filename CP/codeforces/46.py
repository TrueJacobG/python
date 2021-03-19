i = input().split(" ")
red = int(i[0])
blue = int(i[1])


if red > blue:
    rest = (red - blue)//2
    lower = blue
else:
    rest = (blue - red)//2
    lower = red

print(str(lower) + " " + str(rest))
