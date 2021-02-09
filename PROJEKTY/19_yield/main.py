# Generatory

def gen():
    i = 0
    while i < 5:
        yield i
        # coś jak return ale nie przerywa pętli
        i += 1


for i in gen():
    print(i)
    # można wykorzystać teraz te funkcje by odczytać z niej po kolei te wartości które stworzył generator


print(list(gen()))


def parzyste(x):
    j = 0
    while j < x:
        if j % 2 == 0:
            yield j
        if j % 2 != 0:
            yield j-1
        j += 1


print(list(parzyste(10)))


for h in parzyste(10):
    print(h)