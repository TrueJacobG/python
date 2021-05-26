t = int(input())

words = []
divider = 2

for word in range(t):
    words.append(str(input()))

for w in words:
    result = ""
    if len(w) == 2:
        print(w)
        continue
    substrings = [w[i:i+divider]for i in range(0, len(w), divider)]
    for l in substrings:
        result += l[0]
    list1 = list(result)
    list1[-1] = substrings[-1]
    result = "".join(list1)
    print(result)
