from random import randint, choice


class Ship:
    def __init__(self, length: int, tp: int = 1, x: int = None, y: int = None):
        self._x = x
        self._y = y
        self._length = length
        self._tp = tp
        self._is_move = True
        self._cells = [1] * length

    def set_start_coords(self, x: int, y: int):
        """Установка начальных координат (запись значений в локальные атрибуты _x, _y)"""
        self._x = x
        self._y = y

    def get_start_coords(self):
        """Получение начальных координат корабля в виде кортежа x, y"""
        return self._x, self._y

    def move(self, go: int):
        """Перемещение корабля в направлении его ориентации на go клеток
        (go = 1 - движение в одну сторону на клетку; go = -1 - движение в другую сторону на одну клетку);
        движение возможно только если флаг _is_move = True"""
        if self._is_move:
            if self._tp == 1:
                self._x += go
            if self._tp == 2:
                self._y += 1

    def get_coords_ship(self):
        """Получение списка координат всех палуб коробля"""
        if self._tp == 1:
            return [(self._x + i, self._y) for i in range(self._length)]
        if self._tp == 2:
            return [(self._x, self._y + i) for i in range(self._length)]

    def is_collide(self, ship: object):
        """Проверка на столкновение с другим кораблем ship
        (столкновением считается, если другой корабль или пересекается с текущим или просто соприкасается,
        в том числе и по диагонали); метод возвращает True, если столкновение есть и False - в противном случае"""
        ship_coords1 = self.get_coords_ship()
        ship_coords2 = ship.get_coords_ship()
        for coord1 in ship_coords1:
            x1, y1 = coord1
            for coord2 in ship_coords2:
                x2, y2 = coord2
                if abs(x1 - x2) in (0, 1) and abs(y1 - y2) in (0, 1):
                    return True
        return False

    def is_out_pole(self, size: int):
        """Проверка на выход корабля за пределы игрового поля (size - размер игрового поля, обычно, size = 10);
        возвращается булево значение True, если корабль вышел из игрового поля и False - в противном случае"""
        x_end, y_end = self.get_coords_ship()[-1]
        return not (0 <= self._x < size and 0 <= self._y < size and 0 <= x_end < size and 0 <= y_end < size)

    def __getitem__(self, item: int):
        return self._cells[item]

    def __setitem__(self, key, value):
        self._cells[key] = value

    def __repr__(self):
        return f'{self._length}-х палубный корабль'


class GamePole:
    def __init__(self, size: int = 10):
        self._size = size
        self._ships = []

    def init(self):
        """Начальная инициализация игрового поля; здесь создается список из кораблей (объектов класса Ship):
        однопалубных - 4; двухпалубных - 3; трехпалубных - 2; четырехпалубный - 1
        (ориентация этих кораблей должна быть случайной)"""
        ships_count = {4: 1, 3: 2, 2: 3, 1: 4}
        for k, v in ships_count.items():
            for _ in range(v):
                self._ships.append(Ship(k, tp=randint(1, 2)))
        for i, ship in enumerate(self._ships):
            while True:
                x = randint(0, self._size - 1)
                y = randint(0, self._size - 1)
                ship.set_start_coords(x, y)
                if not any((ship.is_collide(stand_ship) for stand_ship in self._ships[:i])) and not ship.is_out_pole(
                        self._size):
                    break

    def check_ship_can_stand(self, check_ship: Ship):
        """Проверка возможности размещения корабля"""
        return not any(
            (check_ship.is_collide(ship) for ship in self._ships if check_ship != ship)) and not check_ship.is_out_pole(
            self._size)

    def get_ships(self):
        """Возвращает коллекцию _ships"""
        return self._ships

    def move_ships(self):
        """Перемещает каждый корабль из коллекции _ships на одну клетку
        (случайным образом вперед или назад) в направлении ориентации корабля"""
        for ship in self._ships:
            x, y = ship.get_start_coords()
            go = choice((-1, 1))
            ship.move(go)
            if self.check_ship_can_stand(ship):
                continue
            else:
                ship.set_start_coords(x, y)
                ship.move(-go)
                if self.check_ship_can_stand(ship):
                    continue
                else:
                    ship.set_start_coords(x, y)

    def stand_ships_on_pole(self):
        """Размещает корабли на игровом поле, для отображения"""
        game_pole = [[0] * self._size for _ in range(self._size)]
        for ship in self._ships:
            coords = ship.get_coords_ship()
            for i, coord in enumerate(coords):
                x, y = coord
                game_pole[y][x] = ship[i]
        return game_pole

    def show(self):
        """Отображение игрового поля в консоли"""
        game_pole = self.stand_ships_on_pole()
        for row in game_pole:
            print(*row)

    def get_pole(self):
        """Возвращает текущее игровое поле в виде двумерного (вложенного) кортежа размерами size x size элементов"""
        game_pole = self.stand_ships_on_pole()
        return tuple(tuple(row) for row in game_pole)


if __name__ == '__main__':
    SIZE_GAME_POLE = 10

    pole = GamePole(SIZE_GAME_POLE)
    pole.init()
    pole.show()

    pole.move_ships()
    print()
    pole.show()