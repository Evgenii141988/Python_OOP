class Matrix:
    def __init__(self, *args):
        if len(args) == 1:
            lst = args[0]
            self.check_list(lst)
            self.list2D = lst
            self.rows = len(self.list2D)
            self.cols = len(self.list2D[0])
        else:
            self.check_args(args)
            self.rows, self.cols, self.fill_value = args
            self.list2D = [[self.fill_value for _ in range(self.cols)] for _ in range(self.rows)]

    @staticmethod
    def check_list(lst: list):
        row0 = len(lst[0])
        if not (all((len(row) == row0 for row in lst)) and all(
                (isinstance(cell, (int, float)) for row in lst for cell in row))):
            raise TypeError('список должен быть прямоугольным, состоящим из чисел')

    @staticmethod
    def check_args(args: tuple):
        rows, cols, fill_value = args
        if not (isinstance(rows, int) and isinstance(cols, int) and isinstance(fill_value, (int, float))):
            raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')

    def check_index(self, indexes: tuple):
        if not (isinstance(indexes, tuple) and len(indexes) == 2):
            raise IndexError('недопустимые значения индексов')
        i, j = indexes
        if not (isinstance(i, int) and 0 <= i < self.rows and isinstance(j, int) and 0 <= j < self.cols):
            raise IndexError('недопустимые значения индексов')

    def check_value(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('значения матрицы должны быть числами')

    def __getitem__(self, item: tuple):
        self.check_index(item)
        i, j = item
        return self.list2D[i][j]

    def __setitem__(self, key: tuple, value: (int, float)):
        self.check_index(key)
        i, j = key
        self.check_value(value)
        self.list2D[i][j] = value

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return Matrix([[self.list2D[i][j] + other for j in range(self.cols)] for i in range(self.rows)])
        if isinstance(other, Matrix):
            if not (self.rows == other.rows and self.cols == other.cols):
                raise ValueError('операции возможны только с матрицами равных размеров')
            return Matrix(
                [[self.list2D[i][j] + other.list2D[i][j] for j in range(self.cols)] for i in range(self.rows)])

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return Matrix([[self.list2D[i][j] - other for j in range(self.cols)] for i in range(self.rows)])
        if isinstance(other, Matrix):
            if not (self.rows == other.rows and self.cols == other.cols):
                raise ValueError('операции возможны только с матрицами равных размеров')
            return Matrix(
                [[self.list2D[i][j] - other.list2D[i][j] for j in range(self.cols)] for i in range(self.rows)])



if __name__ == '__main__':
    mt = Matrix([[1, 2], [3, 4]])
    res = mt[0, 0]  # 1
    res1 = mt[0, 1]  # 2
    res2 = mt[1, 0]  # 3
    res3 = mt[1, 1]  # 4
    print(res, res1, res2, res3)
