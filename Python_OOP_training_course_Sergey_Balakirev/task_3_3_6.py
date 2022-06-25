class Complex:
    def __init__(self, real: (int, float), img: (int, float)):
        self.__real = real
        self.__img = img

    @property
    def real(self):
        return self.__real

    @real.setter
    def real(self, value):
        self.__real = value

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, value):
        self.__img = value

    def __setattr__(self, key, value):
        if key in ('real', 'img') and not isinstance(value, (int, float)):
            raise ValueError("Неверный тип данных.")
        super().__setattr__(key, value)

    def __abs__(self):
        return (self.real ** 2 + self.img ** 2) ** 0.5


if __name__ == '__main__':
    cmp = Complex(7, 8)
    cmp.real = 3
    cmp.img = 4
    c_abs = abs(cmp)
    print(c_abs)