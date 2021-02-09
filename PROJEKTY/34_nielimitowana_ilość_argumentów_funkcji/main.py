# Nielimitowana ilość parametrów

def funkcja(arg, arg2="Świat", *args, **kwargs):
    print(arg, arg2)
    for x in args:
        print(x)
    for y in kwargs.values():
        print(y)
    i = 0
    while i < len(kwargs):
        print(list(kwargs.items())[i][0] + ": " + list(kwargs.items())[i][1])
        i += 1


funkcja("Hello")

funkcja("Witaj", "Świecie", 1, 3, 4, 56)
# te parametry są trzymane w krotce -> () <-

funkcja("Siemano", "Świecie", autor="Ziooomal", rok="2020")