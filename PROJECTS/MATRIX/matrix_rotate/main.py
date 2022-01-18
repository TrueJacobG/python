from random import randint


def createRandomMatrix(size):
    matrix = []
    for _ in range(size):
        r = []
        for _ in range(size):
            r.append(randint(0, 9))
        matrix.append(r)

    return matrix


def printMatrix(matrix):
    for row in matrix:
        print(row)


def rotateMatrix(matrix, direction="right"):
    rotatedMatrix = []
    if direction == "right":
        for row in range(len(matrix)):
            c = []
            for col in range(len(matrix)-1, -1, -1):
                c.append(matrix[col][row])
            rotatedMatrix.append(c)
        return rotatedMatrix

    if direction == "left":
        for row in range(len(matrix)-1, -1, -1):
            c = []
            for col in range(len(matrix)):
                c.append(matrix[col][row])
            rotatedMatrix.append(c)
        return rotatedMatrix


def main():
    print("MATRIX:")
    matrix = createRandomMatrix(5)
    printMatrix(matrix)

    print("ROTATED:")
    rotatedMatrix = rotateMatrix(matrix, "left")
    printMatrix(rotatedMatrix)


if __name__ == '__main__':
    main()
