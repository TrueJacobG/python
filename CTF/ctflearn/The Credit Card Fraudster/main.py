number = "543210******1234"
divider = 123457

i = 100000
while i < 1000000:
    n = number.replace("******", str(i))
    if int(n) % divider == 0:
        print(n)
        print("#######")
    i += 1
