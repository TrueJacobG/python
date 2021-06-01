import base64


def encodeBase64(s):
    s = s.encode("ascii")
    s = base64.b64encode(s)
    return s


def decodeBase64(s):
    s = base64.b64decode(s)
    return s


print(encodeBase64("cat"))
print(decodeBase64("Y2F0"))
