class Furniture:
    def __init__(self, name: str, weight: (int, float)):
        self._name = name
        self._weight = weight

    def __verify_name(self, name: str):
        if not isinstance(name, str):
            raise TypeError('название должно быть строкой')

    def __verify_weight(self, weight: (int, float)):
        if not (isinstance(weight, (int, float)) and weight > 0):
            raise TypeError('вес должен быть положительным числом')

    def __setattr__(self, key, value):
        if key == '_name':
            self.__verify_name(value)
            super().__setattr__(key, value)
        elif key == '_weight':
            self.__verify_weight(value)
            super().__setattr__(key, value)
        else:
            super().__setattr__(key, value)

    def get_attrs(self):
        return tuple(self.__dict__.values())


class Closet(Furniture):
    def __init__(self, name: str, weight: (int, float), tp: bool, doors: int):
        super().__init__(name, weight)
        self._tp = tp
        self._doors = doors


class Chair(Furniture):
    def __init__(self, name: str, weight: (int, float), height: (int, float)):
        super().__init__(name, weight)
        self._height = height


class Table(Furniture):
    def __init__(self, name: str, weight: (int, float), height: (int, float), square: (int, float)):
        super().__init__(name, weight)
        self._height = height
        self._square = square


if __name__ == '__main__':
    cl = Closet('шкаф-купе', 342.56, True, 3)
    chair = Chair('стул', 14, 55.6)
    tb = Table('стол', 34.5, 75, 10)
    print(tb.get_attrs())
