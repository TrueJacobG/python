from itertools import permutations as permu


def permutations(string):
    perm = permu(list(string))
    result = []
    s = ""
    for i in list(perm):
        for letter in i:
            s += letter
        result.append(s)
        s = ""
    return set(result)


print(sorted(permutations('aabb')))
