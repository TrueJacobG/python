import re

wynik = re.match(r"^(?P<nazwa_labelu>Hello)( (?:W)or(l)d)+(!!|\.|-)$","Hello World World.")

if wynik:
    print("Znalazłem")
    print(wynik.group(0))
    print(wynik.group(2))
    print(wynik.groups())
    print(wynik.group("nazwa_labelu"))
else:
    print("Nie znalazłem znaków")
# na 0 miejscu trzyma cały napis
# na 2 miesjcu ma grupę, w tym wypadku " World"
# .groups wszystkie grupy w krotce
# dzięki temu można pokazać żeby powtarzały się całe grupy wyrazów
# (?P<nazwa_labelu>TutajJestNapis) można dawać im nazwy żeby nie szukać ich po id
# ?: i ten wyraz nie ma indeksu, nie psuje się kolejność
# (!!|-|\.) teraz może stać tu "!!" lub "-" lub ".", można dawać różna ilości znaków w przeciwieństwie do []
