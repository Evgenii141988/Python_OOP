# Подвиг 9. Вам необходимо реализовать, следующую стек подобную структуру из объектов класса ListObject:
# Для этого объявите в программе класс ListObject, объекты которого создаются командой:
# obj = ListObject(data)

# Каждый объект класса ListObject должен содержать локальные свойства:
# next_obj - ссылка на следующий присоединенный объект (если следующего объекта нет, то next_obj = None);
# data - данные объекта в виде строки.
#
# В самом классе ListObject должен быть объявлен метод:
# link(self, obj) - для присоединения объекта obj такого же класса в конец последовательности объектов.
#
# Прочитайте список строк из входного потока командой:
# lst_in = list(map(str.strip, sys.stdin.readlines()))

# Затем, создайте первый объект head_obj класса ListObject и сохраните в нем первую строку из списка lst_in.
# После этого присоедините к head_obj (как это показано на рисунке) последующие объекты класса ListObject с
# соответствующими строками из списка lst_in.
# P.S. В программе что-либо выводить на экран не нужно.
import sys


class ListObject:
    def __init__(self, data: str):
        self.data = data
        self.next_obj = None

    def link(self, obj):
        if self.next_obj is None:
            self.next_obj = obj
        else:
            self.next_obj.link(obj)


if __name__ == '__main__':
    # lst_in = list(map(str.strip, sys.stdin.readlines()))
    lst_in = ['1. Первые шаги в ООП', '1.1 Как правильно проходить этот курс', '1.2 Концепция ООП простыми словами',
              '1.3 Классы и объекты. Атрибуты классов и объектов']
    gen_lst_in = (lst for lst in lst_in)
    head_obj = ListObject(next(gen_lst_in))
    for elm in gen_lst_in:
        head_obj.link(ListObject(elm))
    print(head_obj.data)
