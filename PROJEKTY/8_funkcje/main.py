def kwadratowosc(a, b):
    print(a**b)

kwadratowosc(4,3)


def funkcja_z_argumentem_opcjonalnym(x,y=0):
    print(x+y)

funkcja_z_argumentem_opcjonalnym(1)


def funkcja_z_argumentem_opcjonalnym(x=0,y=0):#nadpisanie funkcji
    return(x+y)
    print("Ta część kodu się nie wykona bo jest po return(instrukcja skoku)")

print(funkcja_z_argumentem_opcjonalnym())


def funkcja1(x):
    return x*x

zmienna = funkcja1#zmienna zyskuje zdolności funkcji

print(zmienna(4))


def funkcja2(f1, x):#funkcja staje się jednym z argumentow
    return f1(x) * x

print(funkcja2(funkcja1,3))


def silnia(x):

    if x == 1 or x == 0:
        return 1
    else:
        return x * silnia(x-1)

print(silnia(3))


