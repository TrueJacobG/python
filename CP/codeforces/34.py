numbers = []
for i in range(0, 5):
    numbers.append(int(input()))

k = numbers[0]
l = numbers[1]
m = numbers[2]
n = numbers[3]
count = numbers[4]


for i in range(1, numbers[4]+1):
    if(i % k != 0 and i % l != 0 and i % m != 0 and i % n != 0):
        count -= 1

print(count)
