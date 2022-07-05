class Track:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.__route = []

    def add_point(self, x, y, speed):
        self.__route.append([x, y, speed])

    def check_indx(self, indx: int):
        if not (isinstance(indx, int) and 0 <= indx < len(self.__route)):
            raise IndexError('некорректный индекс')

    def __getitem__(self, item):
        self.check_indx(item)
        return tuple(self.__route[item][:2]), self.__route[item][2]

    def __setitem__(self, key, value):
        self.check_indx(key)
        self.__route[key][2] = value


if __name__ == '__main__':
    tr = Track(10, -5.4)
    tr.add_point(20, 0, 100)  # первый линейный сегмент: indx = 0
    tr.add_point(50, -20, 80)  # второй линейный сегмент: indx = 1
    tr.add_point(63.45, 1.24, 60.34)  # третий линейный сегмент: indx = 2

    tr[2] = 60
    c, s = tr[2]
    print(c, s)

    res = tr[3]  # IndexError
