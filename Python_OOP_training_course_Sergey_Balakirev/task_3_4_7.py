class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year


class Lib:
    def __init__(self):
        self.book_list = []

    def __add__(self, other: object):
        self.book_list.append(other)
        return self

    def __sub__(self, other: (object, int)):
        if isinstance(other, Book):
            self.book_list.remove(other)
        else:
            self.book_list.pop(other)
        return self

    def __len__(self):
        return len(self.book_list)


if __name__ == '__main__':
    lib = Lib()
    b1 = Book('11.22.63', 'Кинг', 2019)
    b2 = Book('Сияние', 'Кинг', 1997)
    lib = lib + b1
    lib += b2
    lib -= 0
    # lib = lib - b2
    print(lib.book_list)
