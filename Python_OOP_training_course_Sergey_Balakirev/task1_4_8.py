# Подвиг 8. Объявите в программе класс Cart (корзина), объекты которого создаются командой:
#
# cart = Cart()
# Каждый объект класса Cart должен иметь локальное свойство goods - список объектов для покупки.
# Изначально этот список должен быть пустым.
# В классе Cart объявить методы:
# add(self, gd) - добавление товара в корзину, представленного объектом gd;
# remove(self, indx) - удаление товара из корзины по индексу indx;
# get_list(self) - получение товаров корзины в виде списка из строк:
# ['<наименовние_1>: <цена_1>',
# '<наименовние_2>: <цена_2>',
# ...
# '<наименовние_N>: <цена_N>']
# Объявите в программе следующие классы для описания товаров:
# Table - столы;
# TV - телевизоры;
# Notebook - ноутбуки;
# Cup - кружки.
# Объекты этих классов должны создаваться командой:
# gd = ИмяКласса(name, price)
# Каждый объект классов товаров должен содержать локальные свойства:
# name - наименование;
# price - цена.
# Создайте в программе объект cart класса Cart. Добавьте в него два телевизора (TV), один стол (Table),
# два ноутбука (Notebook) и одну кружку (Cup). Названия и цены придумайте сами.
#
# P.S. Отображать на экране ничего не нужно, только создать объекты по указанным требованиям.

class Cart:
    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        self.goods.pop(indx)

    def get_list(self):
        return [f'{good.name}: {good.price}' for good in self.goods]


class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price


if __name__ == '__main__':
    cart = Cart()
    tv1 = TV('LG', 1000)
    tv2 = TV('Philips', 2000)
    table = Table('Ikea', 10)
    laptop1 = Notebook('HP', 1000)
    laptop2 = Notebook('MacBook', 5000)
    cup = Cup('Teacup', 5)
    my_goods = [tv1, tv2, table, laptop1, laptop2, cup]
    for good in my_goods:
        cart.add(good)
    print(cart.get_list())