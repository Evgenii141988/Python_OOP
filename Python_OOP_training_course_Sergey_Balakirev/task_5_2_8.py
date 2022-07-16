class Rect:
    def __init__(self, x: (int, float), y: (int, float), width: (int, float), height: (int, float)):
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def __setattr__(self, key, value):
        if key in ('_x', '_y') and not isinstance(value, (int, float)):
            raise ValueError('некорректные координаты и параметры прямоугольника')
        if key in ('_width', '_height') and not (isinstance(value, (int, float)) and value > 0):
            raise ValueError('некорректные координаты и параметры прямоугольника')
        super().__setattr__(key, value)

    def is_collision(self, rect: object):
        Ax1 = self._x
        Ay1 = self._y
        Ax2 = self._x + self._width
        Ay2 = self._y + self._height
        Bx1 = rect._x
        By1 = rect._y
        Bx2 = rect._x + rect._width
        By2 = rect._y + rect._height
        if Ax1 < Bx2 and Ax2 > Bx1 and Ay1 < By2 and Ay2 > By1:
            raise TypeError('прямоугольники пересекаются')


if __name__ == '__main__':
    lst_rect = [Rect(0, 0, 5, 3), Rect(6, 0, 3, 5), Rect(3, 2, 4, 4), Rect(0, 8, 8, 1)]
    lst_not_collision = []
    n = len(lst_rect)
    for i in range(n):
        try:
            for j in range(n):
                if lst_rect[i] != lst_rect[j]:
                    lst_rect[i].is_collision(lst_rect[j])
        except TypeError:
            continue
        else:
            lst_not_collision.append(lst_rect[i])

    print(lst_not_collision)