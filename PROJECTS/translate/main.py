dictionary = {
    ord("a"): ord("b"),  # ascii code
    ord("b"): ord("c"),
    ord("c"): ord("a")
}

string = "abcdef"

print(string.translate(dictionary))


makeTranslate = string.maketrans("a", "1")
print(string.translate(makeTranslate))
