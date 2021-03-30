l = input().split(" ")
numbers = [int(x) for x in l]
numbers.sort()
a = numbers[3] - numbers[0]
b = numbers[3] - numbers[1]
c = numbers[3] - numbers[2]
print(f'{a} {b} {c}')
