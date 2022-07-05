class IntegerValue:
    def __set_name__(self, owner, name):
        self.name = f'__{name}'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError('возможны только целочисленные значения')
        setattr(instance, self.name, value)


class CellInteger:
    value = IntegerValue()

    def __init__(self, start_value=0):
        self.value = start_value


class CellString:
    def __init__(self, start_value=''):
        self.value = start_value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if not isinstance(value, str):
            raise ValueError('возможны только строковое значения')
        self.__value = value


class TableValues:
    def __init__(self, rows: int, cols: int, cell=None):
        if cell is None:
            raise ValueError('параметр cell не указан')
        self.rows = rows
        self.cols = cols
        self.cells = [[cell() for j in range(self.cols)] for i in range(self.rows)]

    def check_indx(self, indx_i: int, indx_j: int):
        if not (isinstance(indx_i, int) and 0 <= indx_i < self.rows and
                isinstance(indx_j, int) and 0 <= indx_j < self.cols):
            raise IndexError('неверный индекс для доступа к элементам таблицы')

    def __getitem__(self, item: tuple):
        i, j = item
        self.check_indx(i, j)
        return self.cells[i][j].value

    def __setitem__(self, key: tuple, value):
        i, j = key
        self.check_indx(i, j)
        self.cells[i][j].value = value


if __name__ == '__main__':
    table = TableValues(2, 3, cell=CellInteger)
    print(table[0, 1])
    table[1, 1] = 10
    # table[0, 0] = 1.45  # генерируется исключение ValueError

    # вывод таблицы в консоль
    for row in table.cells:
        for x in row:
            print(x.value, end=' ')
        print()
