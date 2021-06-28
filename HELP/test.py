def freqAlphabets(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letters = []
    result = ""

    i = 0
    while i < len(s):
        try:
            if s[i+2] == "#":
                letters.append(int(s[i] + s[i+1]))
                i += 2
                continue
        except:
            pass
        if s[i] == "#":
            i += 1
            continue
        letters.append(int(s[i]))
        i += 1

    for i in letters:
        result += alphabet[i-1]

    return result


print(freqAlphabets("10#11#12"))
