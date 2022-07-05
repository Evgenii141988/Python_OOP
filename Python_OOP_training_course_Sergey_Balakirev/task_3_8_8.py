class Cell:
    def __init__(self):
        self.is_free = True
        self.value = 0

    def __bool__(self):
        return self.is_free


class TicTacToe:
    def __init__(self):
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))

    def clear(self):
        for row in self.pole:
            for cell in row:
                cell.is_free = True
                cell.value = 0

    def check_indx(self, i: (int, slice), j: int):
        if not (isinstance(i, int) and 0 <= i < 3 and isinstance(j, int) and 0 <= j < 3):
            raise IndexError('неверный индекс клетки')

    def __getitem__(self, item: tuple):
        i, j = item
        if not isinstance(i, slice) and not isinstance(j, slice):
            self.check_indx(i, j)
            return self.pole[i][j].value
        if isinstance(i, slice):
            return tuple(self.pole[x][j].value for x in range(3))
        if isinstance(j, slice):
            return tuple(self.pole[i][y].value for y in range(3))

    def __setitem__(self, key: tuple, value: int):
        i, j = key
        self.check_indx(i, j)
        if not self.pole[i][j]:
            raise ValueError('клетка уже занята')
        self.pole[i][j].value = value
        self.pole[i][j].is_free = False


def print_pole(pole):
    for row in pole:
        for cell in row:
            print(cell.value, end=' ')
        print()


if __name__ == '__main__':
    game = TicTacToe()
    game.clear()
    print_pole(game.pole)
    game[0, 0] = 1
    print_pole(game.pole)
    game[1, 0] = 2
    print_pole(game.pole)
    # формируется поле:
    # 1 0 0
    # 2 0 0
    # 0 0 0
    # game[3, 2] = 2  # генерируется исключение IndexError
    if game[0, 0] == 0:
        game[0, 0] = 2
    v1 = game[0, :]  # 1, 0, 0
    print_pole(game.pole)
    v2 = game[:, 0]  # 1, 2, 0
    print(v2)
