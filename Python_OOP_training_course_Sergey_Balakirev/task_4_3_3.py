class Book:
    def __init__(self, title: str, author: str, pages: int, year: int):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year


class DigitBook(Book):
    def __init__(self, title: str, author: str, pages: int, year: int, size: int, frm: str):
        super().__init__(title, author, pages, year)
        self.size = size
        self.frm = frm


if __name__ == '__main__':
    d_book = DigitBook('Learning Python', 'M. Lutz', 2000, 2019, 50, 'pdf')
    print(d_book.__dict__)