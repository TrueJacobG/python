n = int(input())
number = list(input().split())
result = []

for i in range(1, n+1):
    for x in number:
        if int(x) == i:
            result.insert(int(x), number.index(x)+1)
            # insert at index x, IT

print(" ".join(str(element) for element in result))
