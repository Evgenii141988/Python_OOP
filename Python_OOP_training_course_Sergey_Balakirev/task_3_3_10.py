class PolyLine:
    def __init__(self, *args):
        self.coords = list(args)

    def add_coord(self, x, y):
        self.coords.append((x, y))

    def remove_coord(self, indx: int):
        self.coords.pop(indx)

    def get_coords(self):
        return self.coords


if __name__ == '__main__':
    poly = PolyLine((1, 2), (3, 5), (0, 10), (-1, 8))
    poly.add_coord(1, 3)
    poly.remove_coord(0)
    print(poly.get_coords())

