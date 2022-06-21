import numpy
class Point:
    MIN_COORD = 0
    MAX_COORD = 100

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __getattribute__(self, item):
        print('__getattribute__')
        if item == '_Point__x':
            raise ValueError("Private attribute")
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        print('__setattr__')
        if key == 'z':
            raise AttributeError("недопустимое имя атрибута")
        super.__setattr__(self, key, value)
        # self.__dict__[key] = value

    def __getattr__(self, item):
        print(f'__getattr__: {item}')


if __name__ == '__main__':
    pt = Point(1, 2)
    pt.z
    print(pt.MAX_COORD)
