n = int(input())
numbers = list(input())

c0 = numbers.count("0")
c1 = numbers.count("1")

print(max(c0, c1)-min(c0, c1))
