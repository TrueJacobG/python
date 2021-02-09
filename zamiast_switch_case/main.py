
def switcher(x):
    # default
    if(x > 5 or x < 1):
        return "Wrong number"

    return {
        1: "Siema",
        2: "Witam",
        3: "Dzień dobry",
        4: "Dobry wieczór",
        5:  "Dobrej nocy",
    }[x]


print(switcher(2))
