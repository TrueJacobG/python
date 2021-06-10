from collections import OrderedDict


def sortSentence(s: str) -> str:
    result = OrderedDict()

    for word in s.split():
        result[int(word[len(word)-1])-1] = word[:len(word)-1]

    return " ".join(dict(sorted(result.items())).values())


print(sortSentence("is2 sentence4 This1 a3"))
