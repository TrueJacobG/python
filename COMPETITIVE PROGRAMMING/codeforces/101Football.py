def isDangerous(s):
    sCopy = s
    if len(max(s.split("0"))) >= 7:
        return "YES"
    if len(max(sCopy.split("1"))) >= 7:
        return "YES"
    return "NO"


s = input()
print(isDangerous(s))
