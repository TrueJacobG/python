from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    l = deque(l)
    result = []
    while l:
        result.append(l.popleft())
        try:
            result.append(l.pop())
        except:
            break
    print(" ".join(str(x) for x in result))
