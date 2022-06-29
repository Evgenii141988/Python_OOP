class MaxPooling:
    def __init__(self, step=(2, 2), size=(2, 2)):
        self.__step = step
        self.__size = size

    @staticmethod
    def check_valid_matrix(matrix: list) -> bool:
        """Для проверки является ли матрица прямоугольной"""
        return all((len(matrix[0]) == len(row) for row in matrix))

    @staticmethod
    def check_valid_numbers_matrix(matrix: list) -> bool:
        """Для проверки значений матрицы на число"""
        return all(all(type(i) in (float, int) for i in row) for row in matrix)

    @staticmethod
    def get_max_number(a: int, b: int, h_size: int, v_size: int, matrix: list):
        """Для нахождения максимального значения в матрице"""
        return max([matrix[i + a][j + b] for i in range(v_size) for j in range(h_size)])

    def __call__(self, matrix: list):
        if not (self.check_valid_matrix(matrix) and self.check_valid_numbers_matrix(matrix)):
            raise ValueError("Неверный формат для первого параметра matrix.")

        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0
        if rows == 0:
            return [[]]

        h_step, v_step = self.__step
        h_size, v_size = self.__size

        rows_result = (rows - v_size) // v_step + 1
        cols_result = (cols - h_size) // h_step + 1
        result = [[0] * cols_result for _ in range(rows_result)]

        di = 0
        for i in range(0, rows, v_step):
            dj = 0
            for j in range(0, cols, h_step):
                try:
                    result[di][dj] = self.get_max_number(i, j, h_size, v_size, matrix)
                    dj += 1
                except IndexError:
                    di += 1
                    dj += 1
                    break
            di += 1

        return result


if __name__ == '__main__':
    mp = MaxPooling(step=(2, 2), size=(2, 2))
    res = mp([[1, 2, 3], [6, 7, 8], [8, 7, 6]])
    print(res)
