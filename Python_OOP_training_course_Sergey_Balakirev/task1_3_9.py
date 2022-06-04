# Подвиг 9. Из входного потока читаются строки данных с помощью команды:
# lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
# в формате: id, name, old, salary (записанные через пробел). Например:
# 1 Сергей 35 120000
# 2 Федор 23 12000
# 3 Иван 13 1200
# ...
# То есть, каждая строка - это элемент списка lst_in.
# Необходимо в класс DataBase:
# class DataBase:
#     lst_data = []
#     FIELDS = ('id', 'name', 'old', 'salary')
# добавить два метода:
# insert(self, data) - для добавления в список lst_data новых данных из переданного списка строк data;
# select(self, a, b) - для отбора и возврата записей в диапазоне [a; b] по их индексам из списка lst_data.
# Каждая запись в списке lst_data должна быть представлена словарем (добавление с помощью метода insert) в формате:
# {'id': 'номер', 'name': 'имя', 'old': 'возраст', 'salary': 'зарплата'}
# Например:
# {'id': '1', 'name': 'Сергей', 'old': '35', 'salary': '120000'}
# Примечание: в этой задаче число элементов в строке (разделенных пробелом) всегда совпадает с
# числом полей в коллекции FIELDS.
# P. S. Ваша задача только добавить два метода в класс DataBase.
# Sample Input:
# 1 Сергей 35 120000
# 2 Федор 23 12000
# 3 Иван 13 1200

import sys

# программу не менять, только добавить два метода
# lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
lst_in = ['1 Сергей 35 120000', '2 Федор 23 12000', '3 Иван 13 1200']


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def insert(self, data):
        for mean in data:
            self.lst_data.append(dict(zip(self.FIELDS, mean.split())))

    def select(self, a, b):
        return self.lst_data[a:b + 1]


if __name__ == '__main__':
    db = DataBase()
    db.insert(lst_in)
    print(db.__dict__)