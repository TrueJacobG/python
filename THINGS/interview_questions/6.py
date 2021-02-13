def czyPalindrom(string):
    string.upper()
    l = len(string)
    yes = 0
    for i in range(0, (l-1)//2):
        if string[i] == string[l-1-i]:
            yes += 1
    if yes == (l-1)//2:
        return "YES"
    else:
        return "NO"


def isPalindrom(string):
    x = ''.join(reversed(string))
    if x == string:
        return "YES"
    else:
        return "NO"
