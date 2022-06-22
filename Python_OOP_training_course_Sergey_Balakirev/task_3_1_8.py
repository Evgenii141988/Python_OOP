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
        self.__radius = value

    def __setattr__(self, key, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Неверный тип присваиваемых данных.")
        if key == 'radius' and value <= 0:
            return
        if key == '_Circle__radius' and value <= 0:
            raise TypeError("Неверный тип присваиваемых данных.")
        super().__setattr__(key, value)

    def __getattr__(self, item):
        return False


if __name__ == '__main__':
    circle = Circle(10.5, 7, 22)
    circle.radius = -10  # прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
    x, y = circle.x, circle.y
    res = circle.name  # False, т.к. атрибут name не существует
