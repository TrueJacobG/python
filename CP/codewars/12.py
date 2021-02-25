def in_array(array1, array2):
    helper = []
    for word1 in array1:
        for word2 in array2:
            if word1 in word2:
                helper.append(word1)
    r = []
    for word in helper:
        if word in r:
            continue
        else:
            r.append(word)
    r.sort()
    return r


print(in_array(["live", "arp", "strong"], [
      "lively", "alive", "harp", "sharp", "armstrong"]))
print(in_array(["arp", "mice", "bull"], [
      "lively", "alive", "harp", "sharp", "armstrong"]))
