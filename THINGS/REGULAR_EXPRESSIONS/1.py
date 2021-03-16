from re import search

regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])[A-Za-z\d]{6,}$"
# ^ start
# [^0-9] without numbers
# (?=.*[]) any thing of this set wherever you want
# [] set
# [A-Za-z\d] only alphanumeric
# {1, } at leat 1 symbol

if search(regex, "Tekst1"):
    print("Yes")
else:
    print("No")
