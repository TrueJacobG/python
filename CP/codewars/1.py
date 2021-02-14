def alphabet_position(text):
    if not any(c.isalpha() for c in text):
        return ""
    result = ""
    text = text.lower()
    text = text.replace(" ", "").replace(".", "").replace("'", "")
    for letter in text:
        it = ord(letter) - 96
        result += f"{it} "
    result = result[:-1:]
    return result


print(alphabet_position("'.asdfadf"))
