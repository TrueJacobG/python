prime = 0
for i in range(100, 200):
    for j in range(2, i):
        if i % j == 0:
            break
        else:
            prime += 1
    if prime == i - 2:
        print(i)
    prime = 0


for n in range(100, 200):
    if all(n % i != 0 for i in range(2, n)):
        print(f"Prime number is {n}")
