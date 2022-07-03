import sys


class BookStudy:
    def __init__(self, name: str, author: str, year: int):
        self.name = name
        self.author = author
        self.year = year

    def __hash__(self):
        return hash((self.name, self.author))

    def __eq__(self, other: object):
        if not isinstance(other, BookStudy):
            raise TypeError('Объекты сравнения должны иметь тип BookStudy')
        return hash(self) == hash(other)


if __name__ == '__main__':
    lst_in = list(map(str.strip, sys.stdin.readlines()))
    lst_bs = []
    for string in lst_in:
        name, author, year = string.split('; ')
        lst_bs.append(BookStudy(name, author, year))
    unique_books = len(set(lst_bs))
