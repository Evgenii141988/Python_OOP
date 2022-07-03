from math import sqrt


class Side:
    def __set_name__(self, owner, name):
        self.name = f'_{name}'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("длины сторон треугольника должны быть положительными числами")
        setattr(instance, self.name, value)


class Triangle:
    a = Side()
    b = Side()
    c = Side()

    def __init__(self, a: (int, float), b: (int, float), c: (int, float)):
        if not all((a < b + c, b < a + c, c < a + b)):
            raise ValueError("с указанными длинами нельзя образовать треугольник")
        self.a = a
        self.b = b
        self.c = c

    def __len__(self):
        return self.a + self.b + self.c

    def __call__(self, *args, **kwargs):
        p = len(self) / 2
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))


