class SellItem:
    def __init__(self, name: str, price: (int, float)):
        self.name = name
        self.price = price


class House(SellItem):
    def __init__(self, name: str, price: (int, float), material: str, square: float):
        super().__init__(name, price)
        self.material = material
        self.square = square


class Flat(SellItem):
    def __init__(self, name: str, price: (int, float), size: float, rooms: int):
        super().__init__(name, price)
        self.size = size
        self.rooms = rooms


class Land(SellItem):
    def __init__(self, name: str, price: (int, float), square: float):
        super().__init__(name, price)
        self.square = square


class Agency:
    def __init__(self, name: str):
        self.name = name
        self.__objects = []

    def add_object(self, obj: object):
        self.__objects.append(obj)

    def remove_object(self, obj: object):
        self.__objects.remove(obj)

    def get_objects(self):
        return self.__objects

    def __iter__(self):
        return (obj for obj in self.__objects)


if __name__ == '__main__':
    ag = Agency("Рога и копыта")
    ag.add_object(Flat("квартира, 3к", 10000000, 121.5, 3))
    ag.add_object(Flat("квартира, 2к", 8000000, 74.5, 2))
    ag.add_object(Flat("квартира, 1к", 4000000, 54, 1))
    ag.add_object(House("дом, крипичный", price=35000000, material="кирпич", square=186.5))
    ag.add_object(Land("участок под застройку", 3000000, 6.74))
    for obj in ag.get_objects():
        print(obj.name)

    for obj in ag:
        print(obj.name)

    lst_houses = list(filter(lambda x: isinstance(x, House), ag.get_objects()))  # выделение списка домов
    print(lst_houses)


