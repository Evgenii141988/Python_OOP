# Большой подвиг 10. Объявите два класса:
# Cell - для представления клетки игрового поля;
# GamePole - для управления игровым полем, размером N x N клеток.
#
# С помощью класса Cell предполагается создавать отдельные клетки командой:
# c1 = Cell(around_mines, mine)
# Здесь around_mines - число мин вокруг данной клетки поля; mine - булева величина (True/False), означающая наличие
# мины в текущей клетке. При этом, в каждом объекте класса Cell должны создаваться локальные свойства:
# around_mines - число мин вокруг клетки (начальное значение 0);
# mine - наличие мины в текущей клетке (True/False);
# fl_open - открыта/закрыта клетка - булево значение (True/False). Изначально все клетки закрыты (False).
#
# С помощью класса GamePole должна быть возможность создавать квадратное игровое поле с числом клеток N x N:
# pole_game = GamePole(N, M)
# Здесь N - размер поля; M - общее число мин на поле. При этом, каждая клетка представляется объектом класса Cell и
# все объекты хранятся в двумерном списке N x N элементов - локальном свойстве pole объекта класса GamePole.
# В классе GamePole должны быть также реализованы, следующие методы:
#
# init() - инициализация поля с новой расстановкой M мин (случайным образом по игровому полю, разумеется каждая мина
# должна находиться в отдельной клетке).
# show() - отображение поля в консоли в виде таблицы чисел открытых клеток (если клетка не открыта,
# то отображается символ #).
#
# При создании экземпляра класса GamePole в его инициализаторе следует вызывать метод init() для первоначальной
# инициализации игрового поля.
#
# В классе GamePole могут быть и другие вспомогательные методы.
#
# Создайте экземпляр pole_game класса GamePole с размером поля N = 10 и числом мин M = 12. Вызовите метод init()
# для расстановки мин по игровому полю и подсчета числа мин вокруг клеток без мин.
#
# P.S. На экран в программе ничего выводить не нужно.
#
from random import randint


class Cell:
    def __init__(self, around_mines=0, mine=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False


class GamePole:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.init()

    def init(self):
        self.pole = [[Cell() for _ in range(self.N)] for _ in range(self.N)]
        self.get_random_coords()
        self.installation_mine()
        self.count_mine_around_cell()

    def count_mine_around_cell(self):
        """Метод подсчета мин вокруг пустой клетки"""
        for x, row in enumerate(self.pole):
            for y, cell in enumerate(row):
                if not cell.mine:
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            try:
                                if self.pole[x + i][y + j].mine and x + i >= 0 and y + j >= 0:
                                    cell.around_mines += 1
                            except IndexError:
                                cell.around_mines += 0

    def get_random_coords(self):
        """Метод получения случайных координат"""
        self.coords = []
        while len(self.coords) < self.M:
            x, y = randint(0, self.N - 1), randint(0, self.N - 1)
            if (x, y) not in self.coords:
                self.coords.append((x, y))

    def installation_mine(self):
        """Метод установки мин"""
        for x, y in self.coords:
            self.pole[x][y].mine = True

    def show(self):
        """Метод отображение поля в консоли в виде таблицы чисел открытых клеток"""
        for row in self.pole:
            for cell in row:
                if not cell.fl_open:
                    print('#', end='')
                else:
                    print(cell.around_mines, end='')
            print()


if __name__ == '__main__':
    pole_game = GamePole(10, 12)
    pole_game.init()
    pole_game.show()
