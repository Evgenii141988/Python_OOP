class FloatValue:

    @classmethod
    def verify_value(cls, value):
        if not isinstance(value, float):
            raise TypeError("Присваивать можно только вещественный тип данных.")

    def __set_name__(self, owner, name):
        self.name = f'_{name}'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_value(value)
        setattr(instance, self.name, value)


class Cell:
    value = FloatValue()

    def __init__(self, value: float = 0.0):
        self.value = value


class TableSheet:
    def __init__(self, n: int, m: int):
        self.cells = [[Cell() for _ in range(m)] for _ in range(n)]


if __name__ == '__main__':
    gen_num = (float(i) for i in range(1, 16))
    table = TableSheet(5, 3)
    for row in table.cells:
        for cell in row:
            cell.value = next(gen_num)
            print(cell.value)

    # l = [[Cell() for _ in range(5)] for _ in range(3)]
    #
    # print(*l, sep='\n')
