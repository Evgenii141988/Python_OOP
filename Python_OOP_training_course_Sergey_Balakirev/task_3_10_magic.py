from random import randint


class Cell:
    def __init__(self):
        self.value = 0

    def __bool__(self):
        return self.value == 0


class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

    def __init__(self):
        self.__size = 3
        self.pole = tuple(tuple(Cell() for _ in range(self.__size)) for _ in range(self.__size))
        self.__is_human_win = False
        self.__is_computer_win = False
        self.__is_draw = False


    @property
    def is_human_win(self):
        return self.__is_human_win

    @is_human_win.setter
    def is_human_win(self, value: bool):
        self.__is_human_win = value

    @property
    def is_computer_win(self):
        return self.__is_computer_win

    @is_computer_win.setter
    def is_computer_win(self, value: bool):
        self.__is_computer_win = value

    @property
    def is_draw(self):
        return self.__is_draw

    @is_draw.setter
    def is_draw(self, value: bool):
        self.__is_draw = value

    def check_index(self, indexes: tuple):
        if not (isinstance(indexes, tuple) and len(indexes) == 2):
            raise IndexError('некорректно указанные индексы')
        i, j = indexes
        if not (isinstance(i, int) and 0 <= i < self.__size and isinstance(j, int) and 0 <= j < self.__size):
            raise IndexError('некорректно указанные индексы')

    def __getitem__(self, item: tuple):
        self.check_index(item)
        i, j = item
        return self.pole[i][j].value

    def __setitem__(self, key: tuple, value: int):
        self.check_index(key)
        i, j = key
        self.pole[i][j].value = value
        if self.__check_win_combination(value):
            if value == 1:
                self.is_human_win = True
            else:
                self.is_computer_win = True
        else:
            if all((self.pole[i][j].value in (1, 2) for i in range(self.__size) for j in range(self.__size))):
                self.is_draw = True

    def init(self):
        self.is_human_win = False
        self.is_computer_win = False
        self.is_draw = False
        for i in range(self.__size):
            for j in range(self.__size):
                self.pole[i][j].value = 0

    def show(self):
        for i in range(self.__size):
            for j in range(self.__size):
                print(self.pole[i][j].value, end=' ')

            print()
        print()

    def human_go(self):
        while True:
            try:
                x, y = tuple(int(i) for i in input('Введите координаты клетки (два числа через пробел): ').split())
            except ValueError:
                raise IndexError('некорректно указанные индексы')
            if self.pole[x][y]:
                self[x, y] = self.HUMAN_X
                break
            print('Клетка занята!!!')

    def computer_go(self):
        while True:
            x = randint(0, 2)
            y = randint(0, 2)
            if self.pole[x][y]:
                self[x, y] = self.COMPUTER_O
                break

    def __check_win_combination(self, value: int):
        result = []
        for i in range(self.__size):
            result.append(all([self.pole[i][j].value == value for j in range(self.__size)]))
        for j in range(self.__size):
            result.append(all([self.pole[i][j].value == value for i in range(self.__size)]))
        result.append(all([self.pole[i][i].value == value for i in range(self.__size)]))
        result.append(all([self.pole[i][self.__size - i - 1].value == value for i in range(self.__size)]))
        return any(result)

    def __bool__(self):
        if self.is_human_win or self.is_computer_win or self.is_draw:
            return False
        return True


if __name__ == '__main__':
    game = TicTacToe()
    game.init()
    step_game = 0
    while game:
        game.show()

        if step_game % 2 == 0:
            game.human_go()
        else:
            game.computer_go()

        step_game += 1

    game.show()

    if game.is_human_win:
        print("Поздравляем! Вы победили!")
    elif game.is_computer_win:
        print("Все получится, со временем")
    else:
        print("Ничья.")
