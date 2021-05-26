def duplicate_count(text):
    result = 0
    helper = ""
    text = text.lower()
    for letter in text:
        if text.count(letter) > 1:
            if helper.find(letter) == -1:
                helper += letter
                result += 1
                text.replace(letter, "")
    return result


print(duplicate_count("abcdeaa"))
print(duplicate_count("abcdeaB"))
print(duplicate_count("Indivisibilities"))
