import sys


class Test:
    def __init__(self, n):
        self.n = n


n = [x for x in range(1000000)]
n_obj = Test([x for x in range(1000000)])
# print(n_obj.n)

print(sys.getsizeof(n))
print(sys.getsizeof(n_obj))
# 8697456
# 48
