class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    @classmethod
    def __check_value(cls, number: int):
        return cls.MIN_DIMENSION <= number <= cls.MAX_DIMENSION

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        if self.__check_value(value):
            self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        if self.__check_value(value):
            self.__b = value

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        if self.__check_value(value):
            self.__c = value

    def __le__(self, other: object):
        if not isinstance(other, Dimensions):
            raise TypeError('Объекты сравнения должны иметь тип Dimensions')
        return self.a * self.b * self.c <= other.a * other.b * other.c

    def __lt__(self, other: object):
        if not isinstance(other, Dimensions):
            raise TypeError('Объекты сравнения должны иметь тип Dimensions')
        return self.a * self.b * self.c < other.a * other.b * other.c


class ShopItem:
    def __init__(self, name: str, price: (int, float), dim: object):
        self.name = name
        self.price = price
        self.dim = dim


if __name__ == '__main__':
    lst_shop = [ShopItem('кеды', 1024, Dimensions(40, 30, 120)),
                ShopItem('зонт', 500.24, Dimensions(10, 20, 50)),
                ShopItem("холодильник", 40000, Dimensions(2000, 600, 500)),
                ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200))]

    lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim)
    print(lst_shop)
    print(lst_shop_sorted)
