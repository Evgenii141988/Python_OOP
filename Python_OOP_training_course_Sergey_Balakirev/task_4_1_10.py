class Vector:
    def __init__(self, *args):
        self.coords = args

    def check_size(self, vector: object):
        if not len(self.coords) == len(vector.coords):
            raise TypeError('размерности векторов не совпадают')

    def get_coords(self):
        return self.coords

    def __add__(self, other: object):
        self.check_size(other)
        coords = tuple(self.coords[i] + other.coords[i] for i in range(len(self.coords)))
        if all((isinstance(i, int) for i in coords)):
            return VectorInt(*coords)
        return Vector(*coords)

    def __sub__(self, other: object):
        self.check_size(other)
        coords = tuple(self.coords[i] - other.coords[i] for i in range(len(self.coords)))
        if all((isinstance(i, int) for i in coords)):
            return VectorInt(*coords)
        return Vector(*coords)


class VectorInt(Vector):
    def __init__(self, *args):
        if not all((isinstance(i, int) for i in args)):
            raise ValueError('координаты должны быть целыми числами')
        super().__init__(*args)


if __name__ == '__main__':
    v1 = Vector(1, 2.0, 3)
    v2 = Vector(3, 4, 5)
    v = v1 + v2
    print(type(v))