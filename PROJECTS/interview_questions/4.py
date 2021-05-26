# fibonacci series

x = 0
y = 1
result = 0

for i in range(1, 10):
    result = x + y
    x = y
    y = result
    print(result)
