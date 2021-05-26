# Klasy - właściwości

class Kontobankowe:
    __stan = 0

    @property
    def stan_konta(self):
        return self.__stan

    @stan_konta.getter
    def stan_konta(self):
        # kiedy chcesz pobrac właściwość odpali się to
        return "Stan konta: " + str(self.__stan) + "zł"

    @stan_konta.setter
    def stan_konta(self, wartosc):
        # kiedy chcesz zmienić wartość to przekazuje tutaj
        self.__stan += wartosc


konto = Kontobankowe()
print(konto.stan_konta)
# teraz ta metoda jest właściwością i wywołuje się ją bez nawiasów
# nie można teraz zmienieć wartości zmiany konta
# @properties -> tylko do odczytu
# @stan_konta.getter kiedy pobierasz właściwość to odpala się to w 1 kolejności

konto.stan_konta = 50
print(konto.stan_konta)
# zmieniamy wartość więc odpala się @stan_konta.setter
