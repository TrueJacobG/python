def kreski(szczyt, znak="-"):
    if(type(znak) == int and szczyt < 10):
        for x in range(1, szczyt):
            print(x * str(x))
        for x in range(szczyt, 0, -1):
            print(x * str(x))

    elif(type(znak) == int and szczyt >= 10):
        for x in range(1, szczyt):
            print(x * str(0))
        for x in range(szczyt, 0, -1):
            print(x * str(0))

    else:
        for x in range(1, szczyt):
            print(x * str(znak))
        for x in range(szczyt, 0, -1):
            print(x * str(znak))
