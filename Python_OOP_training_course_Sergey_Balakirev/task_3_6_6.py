import sys
import re


class ShopItem:
    def __init__(self, name: str, weight: (int, float), price: (int, float)):
        self.name = name
        self.weight = weight
        self.price = price

    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))

    def __eq__(self, other: object):
        return hash(self) == hash(other)


def get_int_or_float_number(string: str) -> (int, float):
    return int(string) if string.isdigit() else float(string)


if __name__ == '__main__':
    # lst_in = list(map(str.strip, sys.stdin.readlines()))
    lst_in = ['Системный блок: 1500 75890.56', 'Монитор Samsung rerr: 2000 34000', 'Клавиатура: 200.44 545',
              'Монитор Samsung: 2000 34000']
    reg = r'[A-Za-zА-Яа-я\s]+:|\s*[\d\.]*\s*'
    gen_lst = ([elm.strip(': ') for elm in re.findall(reg, s) if elm not in ('', ' ')] for s in lst_in)
    lst_obj = [ShopItem(elm[0], get_int_or_float_number(elm[1]), get_int_or_float_number(elm[2])) for elm in gen_lst]
    shop_items = {}
    for obj in lst_obj:
        if obj not in shop_items:
            shop_items[obj] = [obj, 1]
        else:
            shop_items[obj][1] += 1
    print(shop_items)
