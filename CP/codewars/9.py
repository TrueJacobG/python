def rgb(r, g, b):
    if r > 255:
        r = 255
    elif r < 0:
        r = 0
    if g > 255:
        g = 255
    elif g < 0:
        g = 0
    if b > 255:
        b = 255
    elif b < 0:
        b = 0
    r = str(hex(r)).replace("0x", "").upper()
    if not len(r) == 2:
        r = "0"+r
    g = str(hex(g)).replace("0x", "").upper()
    if not len(g) == 2:
        g = "0"+g
    b = str(hex(b)).replace("0x", "").upper()
    if not len(b) == 2:
        b = "0"+b
        
    return r+g+b


print(rgb(0, 0, 0))  # "000000"
print("XXXXXXXXXXXXXX")
print(rgb(1, 2, 3))  # "010203"
print("XXXXXXXXXXXXXX")
print(rgb(255, 255, 255))  # "FFFFFF"
print("XXXXXXXXXXXXXX")
print(rgb(254, 253, 252))  # "FEFDFC"
print("XXXXXXXXXXXXXX")
print(rgb(-20, 275, 125))  # "00FF7D"
print("XXXXXXXXXXXXXX")
print(rgb(23, 69, 11))  # "000000"
