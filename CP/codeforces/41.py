n = int(input())
figures = []

for i in range(0, n):
    figures.append(input())

result = 0
for name in figures:
    if name == "Tetrahedron":
        result += 4
    if name == "Cube":
        result += 6
    if name == "Octahedron":
        result += 8
    if name == "Dodecahedron":
        result += 12
    if name == "Icosahedron":
        result += 20

print(result)
