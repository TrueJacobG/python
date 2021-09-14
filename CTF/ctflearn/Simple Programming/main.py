# number of 0's in line -> modulo 3 == 0
# or
# number of 1's in line -> modulo 2 == 0
result = 0
with open("data.txt", "r") as f:
    for line in f:
        if line.count("0") % 3 == 0:
            result += 1
        elif line.count("1") % 2 == 0:
            result += 1

print(result)
