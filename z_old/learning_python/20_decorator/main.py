# Dekoratory

def decorator(func):
    def wrapper():
        print("+++++")
        func()
        print("+++++")
    return wrapper


# wrapper -> Opakowanie


def hello():
    print("Hello world!")


udekorowane = decorator(hello)

# przypisanie funkcji do zmiennej
# WAŻNE! Nie podaje się wtedy nawiasów
# np. def witaj():
# np. siema = witaj
# np. siema()  <- robi to co funkcja witaj
# tworzy się jakby funkcja z innej funkcji ozdobiona dekoratorem

udekorowane()


# Funkcja zostanie udekorowana funkcą dekorator GIGA KOX
@decorator
def witaj():
    print("Witaj świecie!")


witaj()
