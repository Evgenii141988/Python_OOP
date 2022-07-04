class Vector:
    def __init__(self, *args):
        self.coords = list(args)

    def check_coords(self, other):
        if len(self.coords) != len(other.coords):
            raise ArithmeticError('размерности векторов не совпадают')

    def __add__(self, other):
        self.check_coords(other)
        return Vector(*[elm + other.coords[i] for i, elm in enumerate(self.coords)])

    def __sub__(self, other):
        self.check_coords(other)
        return Vector(*[elm - other.coords[i] for i, elm in enumerate(self.coords)])

    def __mul__(self, other):
        self.check_coords(other)
        return Vector(*[elm * other.coords[i] for i, elm in enumerate(self.coords)])

    def __iadd__(self, other):
        if isinstance(other, Vector):
            self.check_coords(other)
            self.coords = [elm + other.coords[i] for i, elm in enumerate(self.coords)]
        else:
            self.coords = [elm + other for elm in self.coords]
        return self

    def __isub__(self, other):
        if isinstance(other, Vector):
            self.check_coords(other)
            self.coords = [elm - other.coords[i] for i, elm in enumerate(self.coords)]
        else:
            self.coords = [elm - other for elm in self.coords]
        return self

    def __eq__(self, other):
        return all([elm == other.coords[i] for i, elm in enumerate(self.coords)])


if __name__ == '__main__':
    v1 = Vector(1, 2, 3)
    v2 = Vector(1, 2, 3)
    print(v1 + v2)
