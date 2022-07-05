class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.__things = []

    def __check_weight(self, new_obj, old_obj=None):
        old_obj_weight = 0 if old_obj is None else old_obj.weight
        if sum((obj.weight for obj in self.__things)) + new_obj.weight - old_obj_weight > self.max_weight:
            raise ValueError('превышен суммарный вес предметов')

    def add_thing(self, thing: object):
        self.__check_weight(thing)
        self.__things.append(thing)

    def __check_indx(self, indx: int):
        if not (isinstance(indx, int) and 0 <= indx < len(self.__things)):
            raise IndexError('неверный индекс')

    def __getitem__(self, item: int):
        self.__check_indx(item)
        return self.__things[item]

    def __setitem__(self, key: int, value: object):
        self.__check_indx(key)
        self.__check_weight(value, self.__things[key])
        self.__things[key] = value

    def __delitem__(self, key: int):
        self.__check_indx(key)
        del self.__things[key]


class Thing:
    def __init__(self, name: str, weight: (int, float)):
        self.name = name
        self.weight = weight


if __name__ == '__main__':
    bag = Bag(1000)
    bag.add_thing(Thing('книга', 100))
    bag.add_thing(Thing('носки', 200))
    bag.add_thing(Thing('рубашка', 500))
    # bag.add_thing(Thing('ножницы', 300))  # генерируется исключение ValueError
    print(bag[2].name)  # рубашка
    bag[1] = Thing('платок', 200)
    print(bag[1].name)  # платок
    del bag[0]
    print(bag[0].name)  # платок

    # t = bag[4]  # генерируется исключение IndexError
