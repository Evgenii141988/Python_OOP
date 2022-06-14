class Point:
    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y

    @classmethod
    def __check_value(cls, x):
        return isinstance(x, (int, float))

    def set_coord(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError('Coords must be numbers')

    def get_coord(self):
        return self.__x, self.__y


if __name__ == '__main__':
    pt = Point(1, 2)
    pt.set_coord(3, 4)
    print(pt.get_coord())
    print(dir(pt))
    print(pt._Point__x)
    print(pt._Point__y)
