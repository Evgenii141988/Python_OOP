from math import sqrt


class RadiusVector:
    def __init__(self, *args):
        self.coords = args

    def __setattr__(self, key, value):
        if len(value) == 1:
            super().__setattr__(key, (0,) * value[0])
        else:
            super().__setattr__(key, value)

    def set_coords(self, *args):
        if len(args) >= len(self.coords):
            self.coords = args[:len(self.coords)]
        else:
            self.coords = args + self.coords[len(args):]

    def get_coords(self):
        return self.coords

    def __len__(self):
        return len(self.coords)

    def __abs__(self):
        return sqrt(sum((i ** 2 for i in self.coords)))


if __name__ == '__main__':
    vector3D = RadiusVector(3)
    vector3D.set_coords(3, -5.6, 8)
    a, b, c = vector3D.get_coords()
    vector3D.set_coords(3, -5.6, 8, 10, 11)  # ошибки быть не должно, последние две координаты игнорируются
    vector3D.set_coords(1, 2)  # ошибки быть не должно, меняются только первые две координаты
    res_len = len(vector3D)  # res_len = 3
    res_abs = abs(vector3D)
    print(res_abs)
    print(res_len)
