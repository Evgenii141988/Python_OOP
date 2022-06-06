# Подвиг 4. Объявите три класса геометрических фигур: Line, Rect, Ellipse. Должна быть возможность
# создавать объекты каждого класса, следующими командами:
# g1 = Line(a, b, c, d)
# g2 = Rect(a, b, c, d)
# g3 = Ellipse(a, b, c, d)
# Здесь в качестве аргументов a, b, c, d передаются координаты верхнего правого и нижнего левого углов
# (произвольные числа). В каждом объекте координаты должны сохраняться в локальных свойствах sp (верхний правый угол)
# и ep (нижний левый) в виде кортежей (a, b) и (c, d) соответственно.
# Сформируйте 217 объектов этих классов: для каждого текущего объекта класс выбирается случайно
# (или Line, или Rect, или Ellipse). Координаты также генерируются случайным образом (числовые значения).
# Все объекты сохраните в списке elements.
# В списке elements обнулите координаты объектов только для класса Line.
# P.S. На экран в программе ничего выводить не нужно.
from random import choice, randint


class Line:
    def __init__(self, a, b, c, d):
        self.sp = a, b
        self.ep = c, d


class Rect:
    def __init__(self, a, b, c, d):
        self.sp = a, b
        self.ep = c, d


class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = a, b
        self.ep = c, d


def get_random_classname() -> str:
    return choice(['Line', 'Rect', 'Ellipse'])


def get_random_object(name: str) -> object:
    if name == 'Line':
        return Line
    elif name == 'Rect':
        return Rect
    return Ellipse


def get_random_coords() -> tuple:
    a, b, c, d = randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100)
    return a, b, c, d


if __name__ == '__main__':
    elements = []
    for _ in range(217):
        classname = get_random_classname()
        element = get_random_object(classname)(*get_random_coords())
        elements.append(element)
    for element in elements:
        if isinstance(element, Line):
            element.ep = 0, 0
            element.sp = 0, 0
        print(element.ep, element.sp)
