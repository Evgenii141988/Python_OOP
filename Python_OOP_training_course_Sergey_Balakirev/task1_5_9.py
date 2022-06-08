# Подвиг 9 (на повторение материала). Объявите класс Point для представления точек на плоскости.
# Создавать объекты этого класса предполагается командой:
# pt = Point(x, y)
# Здесь x, y - числовые координаты точки на плоскости (числа), то есть, в каждом объекте этого класса
# создаются локальные свойства x, y, которые хранят конкретные координаты точки.
# Необходимо в классе Point реализовать метод clone(self), который бы создавал новый объект класса Point
# как полную копию текущего объекта (с тем же набором и значениями всех локальных свойств).
# Создайте в программе объект pt класса Point и еще один объект pt_clone через вызов метода clone.
# P.S. В программе на экран ничего выводить не нужно.

class Point:
    __instance = None

    def __new__(cls, *args, **kwargs):
        cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def clone(self):
        return self.__instance


if __name__ == '__main__':
    pt = Point(1, 2)
    pt_clone = pt.clone()
    print(id(pt))
    print(id(pt_clone))
    assert id(pt_clone) != id(pt), "метод clone не создает новый объект"
    pt1 = Point(3, 4)
    pt1_clone = pt1.clone()
    print(id(pt1))
    print(id(pt1_clone))
