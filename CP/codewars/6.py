import string


def is_pangram(s):
    s = s.lower()
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in s:
            return False
    return True


print(is_pangram("The quick, brown fox jumps over the lazy dog!"))
