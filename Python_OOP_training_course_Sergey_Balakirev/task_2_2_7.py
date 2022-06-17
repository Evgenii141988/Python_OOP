class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    @classmethod
    def check_coord(cls, coord: (int, float)) -> bool:
        return isinstance(coord, (int, float)) and cls.MIN_COORD <= coord <= cls.MAX_COORD

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if self.check_coord(value):
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if self.check_coord(value):
            self.__y = value

    @staticmethod
    def norm2(vector: object):
        return vector.x ** 2 + vector.y ** 2


if __name__ == '__main__':
    v1 = RadiusVector2D()  # радиус-вектор с координатами (0; 0)
    v2 = RadiusVector2D(1)  # радиус-вектор с координатами (1; 0)
    v3 = RadiusVector2D(1, 2)  # радиус-вектор с координатами (1; 2)
    print(v1.norm2(v1))
    print(v1.norm2(v2))
    print(v1.norm2(v3))
