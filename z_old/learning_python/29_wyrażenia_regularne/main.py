# Wyrażenia regularne

import re


napis9 = r"pomarancza\n\n\n\t"
# r -> raw, przed napisam sprawia że czyta np. \n jako tekst zwykły

napis1 = r"pomarancza"
# pattern

tekst = r"jabłkopomaranczaowocelesnemmmm"

print(re.match(napis1, tekst))
# none jeśli nie zaczyna się od patternu
# objekt jeśli zaczyna się danym wzorem

print(re.match(r".*" + napis1 + r".*", tekst))
# sprawdzi również czy jest w środku wzór


if re.search(napis1, tekst):
    print("Znajduje się w nim!")
else:
    print("Nie ma tego!")


print(re.findall(napis1, tekst))
# szuka w tekście wzorów i zwraca tablicę ze wzorami
# np. znajdowanie wszystkich słów zaczynających się dużą literą

znalazlem = re.search(napis1, tekst)
# oczywiście traktuje się jak obiekt
print(znalazlem.group())

print(znalazlem.start())
# gdzie się zaczyna
print(znalazlem.end())
# gdzie kończy
print(znalazlem.span())
# pozycja w krotce

tekst2 = re.sub(napis1, r"ananas", tekst)
print(tekst2)
# podmiana
