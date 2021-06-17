def toLower(s):
    s = list(s)
    for i in range(len(s)):
        if ord(s[i]) >= 65 and ord(s[i]) <= 90:
            s[i] = chr(ord(s[i])+32)
    return "".join(s)


print(toLower("Hello World"))
