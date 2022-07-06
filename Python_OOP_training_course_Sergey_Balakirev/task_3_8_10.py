class SparseTable:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.__cells = {}

    def __add_row_col(self, row: int, col: int):
        """изменяет количество строк и столбцов при добавлении данных"""
        self.rows = row + 1 if row >= self.rows else self.rows
        self.cols = col + 1 if col >= self.cols else self.cols

    def __sub_row_col(self):
        """изменяет количество строк и столбцов при удалении данных"""
        self.rows = max(list(self.__cells), key=lambda x: x[0])[0] + 1
        self.cols = max(list(self.__cells), key=lambda x: x[1])[1] + 1

    def add_data(self, row: int, col: int, data: object):
        """добавляет данные data (объект класса Cell) в таблицу
        по индексам row, col (целые неотрицательные числа)"""
        self.__add_row_col(row, col)
        self.__cells[(row, col)] = data

    def remove_data(self, row: int, col: int):
        """удаляет ячейки (объект класса Cell) с индексами (row, col)"""
        try:
            del self.__cells[(row, col)]
            self.__sub_row_col()
        except KeyError:
            raise IndexError('ячейка с указанными индексами не существует')

    def __getitem__(self, item: tuple):
        try:
            return self.__cells[item].value
        except KeyError:
            raise ValueError('данные по указанным индексам отсутствуют')

    def __setitem__(self, key: tuple, value):
        row, col = key
        if key in self.__cells:
            self.__cells[key].value = value
        else:
            self.__add_row_col(row, col)
            self.__cells[key] = Cell(value)


class Cell:
    def __init__(self, value):
        self.value = value


if __name__ == '__main__':
    st = SparseTable()
    st.add_data(2, 5, Cell("cell_25"))
    st.add_data(0, 0, Cell("cell_00"))
    st[2, 5] = 25  # изменение значения существующей ячейки
    st[11, 7] = 'cell_117'  # создание новой ячейки
    print(st[0, 0])  # cell_00
    st.remove_data(2, 5)
    print(st.rows, st.cols)
    # val = st[2, 5]  # ValueError
    # st.remove_data(12, 3)  # IndexError
