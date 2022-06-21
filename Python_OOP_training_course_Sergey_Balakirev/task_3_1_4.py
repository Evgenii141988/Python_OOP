class Shop:
    def __init__(self, name: str):
        self.name = name
        self.goods = []

    def add_product(self, product: object):
        self.goods.append(product)

    def remove_product(self, product: object):
        self.goods.remove(product)


class Product:
    GEN_NUMBER = 0

    def __init__(self, name: str, weight: (int, float), price: (int, float)):
        Product.GEN_NUMBER += 1
        self.id = Product.GEN_NUMBER
        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, key, value):
        if key == 'id':
            type_attr = int
        elif key == 'name':
            type_attr = str
        elif key in ('weight', 'price'):
            type_attr = (int, float)
        if not isinstance(value, type_attr):
            raise TypeError("Неверный тип присваиваемых данных.")
        super().__setattr__(key, value)

    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")
        super().__delattr__(item)


if __name__ == '__main__':
    shop = Shop("Балакирев и К")
    book = Product("Python ООП", 100, 1024)
    shop.add_product(book)
    shop.add_product(Product("Python", 150, 512))
    for p in shop.goods:
        print(f"{p.name}, {p.weight}, {p.price}")