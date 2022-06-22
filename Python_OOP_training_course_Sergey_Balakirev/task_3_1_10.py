import time


class GeyserClassic:
    MAX_DATE_FILTER = 100

    def __init__(self):
        self.slot_1 = None
        self.slot_2 = None
        self.slot_3 = None

    def __setattr__(self, key, value):
        if key == 'slot_1' and not (value is None or isinstance(value, Mechanical)):
            return
        if key == 'slot_2' and not (value is None or isinstance(value, Aragon)):
            return
        if key == 'slot_3' and not (value is None or isinstance(value, Calcium)):
            return
        super().__setattr__(key, value)

    def add_filter(self, slot_num: int, my_filter: object):
        if slot_num == 1 and self.slot_1 is None:
            self.slot_1 = my_filter
        if slot_num == 2 and self.slot_2 is None:
            self.slot_2 = my_filter
        if slot_num == 3 and self.slot_3 is None:
            self.slot_3 = my_filter

    def remove_filter(self, slot_num):
        if slot_num == 1:
            self.slot_1 = None
        if slot_num == 2:
            self.slot_2 = None
        if slot_num == 3:
            self.slot_3 = None

    def get_filters(self):
        return self.slot_1, self.slot_2, self.slot_3

    def water_on(self):
        return all(self.get_filters()) and all(
            [0 <= (time.time() - fltr.date) <= self.MAX_DATE_FILTER for fltr in self.get_filters()])


class Mechanical:
    def __init__(self, date: float):
        self.__date = date

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value):
        pass


class Aragon:
    def __init__(self, date: float):
        self.__date = date

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value):
        pass


class Calcium:
    def __init__(self, date: float):
        self.__date = date

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value):
        pass


if __name__ == '__main__':
    my_water = GeyserClassic()
    my_water.add_filter(1, Mechanical(time.time()))
    my_water.add_filter(2, Aragon(time.time()))
    w = my_water.water_on()  # False
    print(w)
    my_water.add_filter(3, Calcium(time.time()))
    w = my_water.water_on()  # True
    print(w)
    f1, f2, f3 = my_water.get_filters()  # f1, f2, f3 - ссылки на соответствующие объекты классов фильтров
    print(f1, f2, f3)
    my_water.add_filter(3, Calcium(time.time()))  # повторное добавление в занятый слот невозможно
    my_water.add_filter(2, Calcium(time.time()))  # добавление в "чужой" слот также невозможно
    f1, f2, f3 = my_water.get_filters()
    print(f1, f2, f3)