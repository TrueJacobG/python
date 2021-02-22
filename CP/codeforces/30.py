n = int(input())
result = 0

if n % 2 == 0:
    result = n//2
else:
    result = (((-1)**n)*n//2)


print(result)
