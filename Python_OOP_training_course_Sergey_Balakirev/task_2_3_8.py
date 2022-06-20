class StringValue:

    def __init__(self, min_length=2, max_length=50):
        self.min_length = min_length
        self.max_length = max_length

    def valid_string(self, string: str):
        return isinstance(string, str) and self.min_length <= len(string) <= self.max_length

    def __set_name__(self, owner, name):
        self.name = f'_{name}'

    def __set__(self, instance, value):
        if self.valid_string(value):
            setattr(instance, self.name, value)

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


class PriceValue:
    def __init__(self, max_value=10000):
        self.max_value = max_value

    def valid_number(self, value: (int, float)):
        return isinstance(value, (int, float)) and 0 <= value <= self.max_value

    def __set_name__(self, owner, name):
        self.name = f'_{name}'

    def __set__(self, instance, value):
        if self.valid_number(value):
            setattr(instance, self.name, value)

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


class Product:
    name = StringValue()
    price = PriceValue()

    def __init__(self, name, price):
        self.name = name
        self.price = price


class SuperShop:

    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product: object):
        self.goods.append(product)

    def remove_product(self, product: object):
        self.goods.remove(product)


if __name__ == '__main__':
    shop = SuperShop("У Балакирева")
    shop.add_product(Product("Курс по Python", 0))
    shop.add_product(Product("Курс по Python ООП", 2000))
    for p in shop.goods:
        print(f"{p.name}: {p.price}")
