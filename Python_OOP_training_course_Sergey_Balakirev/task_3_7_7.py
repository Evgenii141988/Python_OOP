class Ellipse:
    def __init__(self, x1=None, y1=None, x2=None, y2=None):
        if all((x1, y1, x2, y2)):
            self.x1 = x1
            self.y1 = y1
            self.x2 = x2
            self.y2 = y2

    def __bool__(self):
        return bool(self.__dict__)

    def get_coords(self):
        if self:
            return self.x1, self.y1, self.x2, self.y2
        raise AttributeError('нет координат для извлечения')


if __name__ == '__main__':
    lst_geom = [Ellipse(), Ellipse(), Ellipse(1, 2, 3, 4), Ellipse(5, 6, 7, 8)]
    for obj in lst_geom:
        if obj:
            obj.get_coords()

