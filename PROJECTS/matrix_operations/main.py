from copy import deepcopy


class Matrix:
    def __init__(self, array=[]):
        if len(array) != 0:
            self.create(array)

    def create(self, array):
        self.array = array
        print("Array created")
        self.set_dimensions()

    def set_dimensions(self):
        self.rows = len(self.array)
        if not all(len(self.array[0]) == len(self.array[i]) for i in range(self.rows)):
            raise "Wrong array!"

        self.cols = len(self.array[0])

        self.square_matrix = self.rows == self.cols
        if self.square_matrix:
            print("Square matrix")

    def print_matrix(self):
        for x in range(self.rows):
            row = ""
            for y in range(self.cols):
                row += str(self.array[x][y]) + " "
            print(row)

    def array_without(self, array, size, x, y):
        new = []
        for i in range(size):
            if i == x:
                continue
            row = []
            for j in range(size):
                if j == y:
                    continue
                row.append(array[i][j])
            new.append(row)

        return new

    def count_determinant(self, array, size):
        if size == 1:
            return array[0][0]

        if size == 2:
            return (array[0][0] * array[1][1]) - (array[0][1] * array[1][0])

        s = 0
        for i in range(size):
            arr = self.array_without(deepcopy(array), size, 0, i)
            s += array[0][i] * ((-1) ** (i)) * \
                self.count_determinant(arr, size-1)

        return s

    def determinant(self):
        if not self.square_matrix:
            raise "You can't count determinant from non square matix"

        self.deter = self.count_determinant(
            deepcopy(self.array), deepcopy(self.rows))

        print("Determinant:")
        print(self.deter)


def main():
    matrix = Matrix()
    matrix.create([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    matrix.print_matrix()
    matrix.determinant()


if __name__ == "__main__":
    main()
