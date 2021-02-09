def funkcja_anonimowa(f, liczba):
    return f(liczba)

print(funkcja_anonimowa(lambda x: x*x, 3))#funkcja anonimowa, lambda


def kwadrat(x):
    return x*x

print(kwadrat(5))


wynik = (lambda x: x*x)(5)#wywołanie funkcji lamda, 2 nawias to argumenty

print(wynik)


wynik2 = lambda x: x*x

print(wynik2(3))


lam = lambda x, y: x*y

print(lam(3,4))

print((lambda x, y: x/y)(9,3))


