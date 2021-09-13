flag = "01000011010101000100011001111011010000100110100101110100010111110100011001101100011010010111000001110000011010010110111001111101"


def divideBinary(binary):
    result = list(binary)
    for i in range(0, len(result), 9):
        result.insert(i, " ")
    return "".join(result)


print(divideBinary(flag))
