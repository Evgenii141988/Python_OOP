class Track:
    def __init__(self, *args):
        if len(args) == 2 and all(type(x) in (int, float) for x in args):
            self.start_x = args[0]
            self.start_y = args[1]
        else:
            self.__points = list(args)

    @property
    def points(self):
        return tuple(self.__points)

    def add_back(self, pt: object):
        self.__points.append(pt)

    def add_front(self, pt: object):
        self.__points.insert(0, pt)

    def pop_back(self):
        self.__points.pop()

    def pop_front(self):
        self.__points.pop(0)


class PointTrack:
    def __init__(self, x: (int, float), y: (int, float)):
        self.x = x
        self.y = y

    def __setattr__(self, key, value):
        if not isinstance(value, (int, float)):
            raise TypeError('координаты должны быть числами')
        super().__setattr__(key, value)

    def __str__(self):
        return f"PointTrack: {self.x}, {self.y}"


if __name__ == '__main__':
    tr = Track(PointTrack(0, 0), PointTrack(1.2, -0.5), PointTrack(2.4, -1.5))
    tr.add_back(PointTrack(1.4, 0))
    tr.pop_front()
    for pt in tr.points:
        print(pt)
