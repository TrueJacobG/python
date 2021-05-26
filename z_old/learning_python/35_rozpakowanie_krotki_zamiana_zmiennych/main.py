a, b = (2, 5)

print(a)
print(b)

a, b = [1, 4]

print(a)
print(b)

# można łatwo przypisać wartości do zmiennych
# 1 element np. list to 1 wartość do 1 zmiennej

x = 10
y = 20
x , y = y, x
# zamiana wartości zmiennych, dużo szybciej niż w innych językach

print(x, y)

start, *wszystko, koniec = (1, 2, 3, 4, 5, 6, 7)

print(start)
print(wszystko)
print(koniec)
