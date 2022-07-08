class Thing:
    ID = 0

    def __init__(self, name: str, price: float):
        Thing.ID += 1
        self.id = Thing.ID
        self.name = name
        self.price = price
        self.weight = None
        self.dims = None
        self.memory = None
        self.frm = None

    def get_data(self):
        return self.id, self.name, self.price, self.weight, self.dims, self.memory, self.frm


class Table(Thing):
    def __init__(self, name: str, price: float, weight: float, dims: tuple):
        Thing.__init__(self, name, price)
        self.weight = weight
        self.dims = dims


class ElBook(Thing):
    def __init__(self, name: str, price: float, memory: int, frm):
        Thing.__init__(self, name, price)
        self.memory = memory
        self.frm = frm


if __name__ == '__main__':
    table = Table("Круглый", 1024, 812.55, (700, 750, 700))
    book = ElBook("Python ООП", 2000, 2048, 'pdf')
    print(table.__dict__)
    print(book.__dict__)
    print(*table.get_data())
    print(*book.get_data())
