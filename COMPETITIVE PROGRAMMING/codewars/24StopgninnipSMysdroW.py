def spin_words(sentence):
    words = sentence.split(" ")
    for index, word in enumerate(words):
        if len(word) >= 5:
            words[index] = word[::-1]
    return " ".join(words)


print(spin_words("Welcome"))
print(spin_words("Welcome to my house"))
