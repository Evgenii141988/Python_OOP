class Book:
    def __init__(self, title: str = '', author: str = '', pages: int = 0, year: int = 0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value):
        if key in ('title', 'author'):
            type_property = str
        elif key in ('pages', 'year'):
            type_property = int
        if not isinstance(value, type_property):
            raise TypeError("Неверный тип присваиваемых данных.")
        super().__setattr__(key, value)


if __name__ == '__main__':
    book = Book('Python ООП', 'Сергей Балакирев', 123, 2022)

