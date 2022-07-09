class Thing:
    def __init__(self, name: str, price: float, weight: float):
        self.name = name
        self.price = price
        self.weight = weight

    def __eq__(self, other: object):
        return (self.name, self.price, self.weight) == (other.name, other.price, other.weight)

    def __hash__(self):
        return hash((self.name, self.price, self.weight))


class DictShop(dict):
    def __init__(self, things: dict = {}):
        if not isinstance(things, dict):
            raise TypeError('аргумент должен быть словарем')
        if things and not all((isinstance(key, Thing)) for key in things.keys()):
            raise TypeError('ключами могут быть только объекты класса Thing')
        super().__init__(things)

    def __setitem__(self, key: object, value):
        if not isinstance(key, Thing):
            raise TypeError('ключами могут быть только объекты класса Thing')
        super().__setitem__(key, value)

    def __iter__(self):
        return super().__iter__()


if __name__ == '__main__':
    th_1 = Thing('Лыжи', 11000, 1978.55)
    th_2 = Thing('Книга', 1500, 256)
    dict_things = DictShop()
    dict_things[th_1] = th_1
    dict_things[th_2] = th_2
    print(dict_things)

    for x in dict_things:
        print(x.name)
