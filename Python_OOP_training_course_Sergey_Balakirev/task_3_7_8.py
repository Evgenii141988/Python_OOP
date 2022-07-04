from random import randint


class Cell:
    def __init__(self):
        self.__is_mine = False
        self.__number = 0
        self.__is_open = False

    @property
    def is_mine(self):
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, value: bool):
        if not type(value) is bool:
            raise ValueError("недопустимое значение атрибута")
        self.__is_mine = value

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value: bool):
        if not (type(value) is int and 0 <= value <= 8):
            raise ValueError("недопустимое значение атрибута")
        self.__number = value

    @property
    def is_open(self):
        return self.__is_open

    @is_open.setter
    def is_open(self, value: bool):
        if not type(value) is bool:
            raise ValueError("недопустимое значение атрибута")
        self.__is_open = value

    def __bool__(self):
        """возвращает True, если клетка закрыта и False - если открыта"""
        return not self.is_open


class GamePole:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, N: int, M: int, total_mines: int):
        self.__N = N
        self.__M = M
        self.__total_mines = total_mines
        self.__pole_cells = [[Cell() for _ in range(self.__M)] for _ in range(self.__N)]

    @property
    def pole(self):
        return self.__pole_cells

    def init_pole(self):
        """инициализация начального состояния игрового поля (расставляет мины и делает все клетки закрытыми)"""
        for i in range(self.__N):
            for j in range(self.__M):
                self.pole[i][j].is_open = False
        self.get_random_coords()
        self.installation_mine()
        self.count_mine_around_cell()

    def open_cell(self, i: int, j: int):
        """открывает ячейку с индексами (i, j); нумерация индексов начинается с нуля;
         метод меняет значение атрибута __is_open объекта Cell в ячейке (i, j) на True"""
        if not (isinstance(i, int) and isinstance(j, int) and 0 <= i <= self.__N - 1 and 0 <= j <= self.__M - 1):
            raise IndexError('некорректные индексы i, j клетки игрового поля')
        self.pole[i][j].is_open = True

    def count_mine_around_cell(self):
        """Метод подсчета мин вокруг пустой клетки"""
        for x, row in enumerate(self.pole):
            for y, cell in enumerate(row):
                if not cell.is_mine:
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            try:
                                if self.pole[x + i][y + j].is_mine and x + i >= 0 and y + j >= 0:
                                    cell.number += 1
                            except IndexError:
                                cell.number += 0

    def get_random_coords(self):
        """Метод получения случайных координат"""
        self.__coords = []
        while len(self.__coords) < self.__total_mines:
            x, y = randint(0, self.__N - 1), randint(0, self.__M - 1)
            if (x, y) not in self.__coords:
                self.__coords.append((x, y))

    def installation_mine(self):
        """Метод установки мин"""
        for x, y in self.__coords:
            self.pole[x][y].is_mine = True

    def show_pole(self):
        """Метод отображение поля в консоли в виде таблицы чисел открытых клеток"""
        for row in self.pole:
            for cell in row:
                if cell:
                    print('#', end='')
                else:
                    print(cell.number, end='')
            print()


if __name__ == '__main__':
    pole = GamePole(10, 20, 10)  # создается поле размерами 10x20 с общим числом мин 10
    pole.init_pole()
    if pole.pole[0][1]:
        pole.open_cell(0, 1)
    if pole.pole[3][5]:
        pole.open_cell(3, 5)
    pole.open_cell(30, 100)  # генерируется исключение IndexError
    pole.show_pole()
