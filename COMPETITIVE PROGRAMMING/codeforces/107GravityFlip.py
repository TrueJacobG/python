n = int(input())
numbers = [int(x) for x in input().split()]
print(" ".join(str(y) for y in sorted(numbers)))
