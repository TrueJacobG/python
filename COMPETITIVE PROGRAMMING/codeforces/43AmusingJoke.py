import sys
gname = input()
rname = input()
mix = list(input())

try:
    for letter1 in gname:
        mix.remove(letter1)
    for letter2 in rname:
        mix.remove(letter2)
except:
    print("NO")
    sys.exit()

if mix == []:
    print("YES")
else:
    print("NO")
