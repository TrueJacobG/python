def checkZeroOnes(s: str) -> bool:
    nulls: int = 0
    ones: int = 0
    nulls_max: int = 0
    ones_max: int = 0

    if s[0] == "1" and len(s) == 1:
        return True
    if s[0] == "0" and len(s) == 1:
        return False

    #if s[0] == "1":
    #    ones += 1
    if s[0] == "0":
        nulls += 1

    for i in range(1, len(s)):
        if s[i-1] == "1" and s[i] == "1":
            if nulls_max < nulls:
                nulls_max = nulls
                nulls = 0
            ones += 1
        if s[i-1] == "0" and s[i] == "0":
            if ones_max < ones:
                ones_max = ones
                ones = 0
            nulls += 1

        if s[i-1] == "0" and s[i] == "1":
            if nulls_max < nulls:
                nulls_max = nulls
                nulls = 0
            ones += 1

        if s[i-1] == "1" and s[i] == "0":
            if ones_max < ones:
                ones_max = ones
                ones = 0
            nulls += 1

    if nulls_max < nulls:
        nulls_max = nulls
    if ones_max < nulls:
        ones_max = ones
    print("N_MAX", nulls_max)
    print("O_MAX", ones_max)

    if ones_max > nulls_max:
        return True
    return False


checkZeroOnes("0111010011")
