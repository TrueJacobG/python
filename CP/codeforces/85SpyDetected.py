k = int(input())

for x in range(k):
    length = int(input())
    numbers = [int(e) for e in input().split()]
    c = numbers.count(numbers[0])
    if c == 1:
        print(1)
    else:
        for n, element in enumerate(numbers):
            if element != numbers[0]:
                print(n+1)
                break
