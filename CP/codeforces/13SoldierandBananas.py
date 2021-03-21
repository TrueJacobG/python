from math import fabs

helper = input().split()
k = int(helper[0])
n = int(helper[1])
w = int(helper[2])

result = 0

for i in range(1, w+1):
    result += k * i
final_result = result - n

if final_result <= 0:
    print(0)
else:
    print(int(final_result))
