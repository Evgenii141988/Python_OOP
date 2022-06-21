class Circle:
    def __init__(self, x: (int, float), y: (int, float), radius: (int, float)):
        self.__x = x
        self.__y = y
        self.__radius = radius

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        print('setter radius')
        self.__radius = value

    def __setattr__(self, key, value):
        print(f'__setter__: {key}')
        if not ((key in ('_Circle__x', '_Circle__y', 'x', 'y') and isinstance(value, (int, float))) or (
                key in ('radius') and isinstance(value, (int, float)) and value > 0)):
            raise TypeError("Неверный тип присваиваемых данных.")
        if not (key in ('_Circle__radius', 'radius') and value <= 0):
            super().__setattr__(key, value)

    def __getattr__(self, item):
        return False


if __name__ == '__main__':
    circle = Circle(10.5, 7, 22)
    print(circle.x)
    circle.x = 6
    circle.radius = -10  # прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
    x, y = circle.x, circle.y
    # circle.radius = 10
    print(circle.radius)
    res = circle.name  # False, т.к. атрибут name не существует
