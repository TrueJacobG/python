def to_camel_case(text):
    text = list(text)
    result = ""
    for i in range(0, len(text)):
        if text[i] != "_" and text[i] != "-":
            result += str(text[i])
        else:
            text[i+1] = text[i+1].upper()
    return "".join(result)


print(to_camel_case('A_cat-was-evil'))
print(to_camel_case("the_stealth_warrior"))
print(to_camel_case("The-Stealth-Warrior"))
print(to_camel_case("A-B-C"))
