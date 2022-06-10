class Point:
    '''Класс для представления координат точек на плоскости'''
    color = 'red'
    circle = 2

    def __new__(cls, *args, **kwargs):
        print(f'Вызов __new__ для {cls} {args} {kwargs}')
        return super().__new__(cls)

    def __init__(self, x=0, y=0):
        print(f'Вызов __init__ для {self}')
        self.x = x
        self.y = y

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y

    def __del__(self):
        print(f'Удаление экземпляра класса{self}')


class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y):
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y

        print(Vector.norm2(self.x, self.y))

    @staticmethod
    def norm2(x, y):
        return x ** 2 + y ** 2


if __name__ == '__main__':
    # Point.color = 'black'
    # a = Point(1, 2)
    # b = Point(3, 4)
    # a.x = 1
    # a.y = 2
    # b.x = 10
    # b.y = 20
    # pt = Point(5, 6)
    # print(pt.x)
    # pt.set_coords(1, 3)
    v = Vector(3, 4)
