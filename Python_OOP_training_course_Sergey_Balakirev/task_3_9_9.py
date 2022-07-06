class TableValues:
    def __init__(self, rows: int, cols: int, type_data=int):
        self.rows = rows
        self.cols = cols
        self.type_data = type_data
        self.__table = tuple(tuple(Cell() for j in range(self.cols)) for i in range(self.rows))

    def check_type(self, value):
        if not isinstance(value, self.type_data):
            raise TypeError('неверный тип присваиваемых данных')

    def check_index(self, indexes: tuple):
        if not (isinstance(indexes, tuple) and len(indexes) == 2):
            raise IndexError('неверный индекс')
        i, j = indexes
        if not (isinstance(i, int) and 0 <= i < self.rows and isinstance(j, int) and 0 <= j < self.cols):
            raise IndexError('неверный индекс')

    def __getitem__(self, item: tuple):
        self.check_index(item)
        x, y = item
        return self.__table[x][y].data

    def __setitem__(self, key: tuple, value):
        self.check_index(key)
        self.check_type(value)
        x, y = key
        self.__table[x][y].data = value

    def __iter__(self):
        return (tuple(self.__table[i][j].data for j in range(self.cols)) for i in range(self.rows))


class Cell:
    def __init__(self, data=0):
        self.__data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value


if __name__ == '__main__':
    table = TableValues(2, 2, str)
    table[0, 0] = '1'
    table[0, 1] = '2'
    table[1, 0] = '3'
    table[1, 1] = '4'
    for row in table:  # перебор по строкам
        for value in row:  # перебор по столбцам
            print(value, end=' ')  # вывод значений ячеек в консоль
        print()
