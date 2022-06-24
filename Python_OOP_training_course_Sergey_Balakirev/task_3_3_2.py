import sys


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Книга: {self.title}; {self.author}; {self.pages}"


if __name__ == '__main__':
    lst_in = list(map(str.strip, sys.stdin.readlines()))
    book = Book(*lst_in)
    print(book)