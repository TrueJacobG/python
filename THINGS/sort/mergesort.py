
def create_array(size=20, maxx=100):
    from random import randint
    return [randint(0, maxx) for _ in range(size)]


def merge(a, b):
    result = []
    id_a = 0
    id_b = 0
    while id_a < len(a) and id_b < len(b):
        if a[id_a] < b[id_b]:
            result.append(a[id_a])
            id_a += 1
        else:
            result.append(b[id_b])
            id_b += 1
    if id_a == len(a):
        result.extend(b[id_b:])
    else:
        result.extend(a[id_a:])
    return result


def merge_sort(a):
    if len(a) <= 1:
        return a

    # podział listy na 2
    left = merge_sort(a[:len(a)//2])
    right = merge_sort(a[len(a)//2:])

    return merge(left, right)


print(merge_sort(create_array()))
