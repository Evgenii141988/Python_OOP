class Integer:
    def __set_name__(self, owner, name):
        self.name = f'_{name}'

    def __set__(self, instance, value):
        print(f'__set__: {self.name} = {value}')
        setattr(instance, self.name, value)

    def __get__(self, instance, owner):
        print(f'__get__: {self.name}')
        return getattr(instance, self.name)


class Point3D:
    x = Integer()
    y = Integer()
    z = Integer()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


if __name__ == '__main__':
    p1 = Point3D(1, 2, 3)
    print(p1.x)
    p1.y = 30
