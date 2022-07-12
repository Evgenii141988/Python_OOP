class ShopInterface:
    def get_id(self):
        raise NotImplementedError('в классе не переопределен метод get_id')


class ShopItem(ShopInterface):
    __ID = 0

    def __init__(self, name: str, weight: (int, float), price: (int, float)):
        ShopItem.__ID += 1
        self._name = name
        self._weight = weight
        self._price = price
        self.__id = ShopItem.__ID

    def get_id(self):
        return self.__id


if __name__ == '__main__':
    item1 = ShopItem("имя1", "вес1", "100")
    item2 = ShopItem("имя2", "вес2", "200")
    print(item1.get_id())
    print(item2.get_id())