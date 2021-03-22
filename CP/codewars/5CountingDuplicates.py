def anagrams(word, words):
    result = []
    for w in words:
        if sorted(w) == sorted(word):
            result.append(w)
    return result


print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
