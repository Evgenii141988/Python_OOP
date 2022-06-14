class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_coords(self):
        return self.__x, self.__y


class Rectangle:
    @classmethod
    def __get_count_args(cls, *args):
        return len(args)

    def __init__(self, *args):
        if self.__get_count_args(args) == 2:
            self.__sp, self.__ep = args
        else:
            x1, y1, x2, y2 = args
            self.__sp = Point(x1, y1)
            self.__ep = Point(x2, y2)

    def set_coords(self, sp, ep):
        self.__sp = sp
        self.__ep = ep

    def get_coords(self):
        return self.__sp, self.__ep

    def draw(self):
        print(f'Прямоугольник с координатами: {self.__sp.get_coords()} {self.__ep.get_coords()}')


if __name__ == '__main__':
    rect = Rectangle(0, 0, 20, 34)
    rect.draw()
