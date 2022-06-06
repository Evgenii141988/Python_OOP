class Point:
    '''Класс для представления координат точек на плоскости'''
    color = 'red'
    circle = 2

    def __init__(self, a, b):
        self.x = a
        self.y = b

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y

    def __del__(self):
        print(f'Удаление экземпляра класса{self}')


if __name__ == '__main__':
    Point.color = 'black'
    a = Point(1, 2)
    b = Point(3, 4)
    a.x = 1
    a.y = 2
    b.x = 10
    b.y = 20
    pt = Point(5, 6)
    pt.set_coords(1, 3)
    print(pt.__dict__)
    print(pt.get_coords())
