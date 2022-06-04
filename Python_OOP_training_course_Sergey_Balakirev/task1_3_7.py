# Подвиг 7. Имеется следующий класс для считывания информации из входного потока:
# import sys
# class StreamReader:
#     FIELDS = ('id', 'title', 'pages')
#
#     def readlines(self):
#         lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
#         sd = StreamData()
#         res = sd.create(self.FIELDS, lst_in)
#         return sd, res
# Которым, затем, можно воспользоваться, следующим образом:
# sr = StreamReader()
# data, result = sr.readlines()
# Необходимо перед классом StreamReader объявить еще один класс StreamData с методом:
# def create(self, fields, lst_values): ...
# который бы на входе получал список полей FIELDS (передается в атрибут fields) и список строк lst_in
# (передается в атрибут lst_values) и формировал бы в объекте класса StreamData локальные свойства с именами
# полей из fields и соответствующими значениями из lst_values.
# Если создание локальных свойств проходит успешно, то метод create() возвращает True, иначе - False. Если
# число полей и число строк не совпадает, то метод create() возвращает False.
# P.S. В программе нужно дополнительно объявить только класс StreamData. Больше ничего делать не нужно.

import sys


class StreamData:
    def create(self, fields, lst_values):
        if len(fields) == len(lst_values):
            for field, value in zip(fields, lst_values):
                setattr(self, field, value)
            return True
        return False


class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        # lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
        lst_in = ['1', '2', '3']
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res


if __name__ == '__main__':
    sr = StreamReader()
    data, result = sr.readlines()