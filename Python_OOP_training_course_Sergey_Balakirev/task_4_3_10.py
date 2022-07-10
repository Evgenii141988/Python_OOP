class ItemAttrs:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getitem__(self, item: int):
        return (self.x, self.y)[item]

    def __setitem__(self, key: int, value: (int, float)):
        self.__dict__[list(self.__dict__)[key]] = value


class Point(ItemAttrs):
    def __init__(self, x, y):
        super().__init__(x, y)


if __name__ == '__main__':
    pt = Point(1, 2.5)
    x = pt[0]  # 1
    y = pt[1]  # 2.5
    pt[0] = 10
