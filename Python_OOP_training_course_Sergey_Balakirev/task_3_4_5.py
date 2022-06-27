class ListMath:
    def __init__(self, lst: list = None):
        if lst is None:
            self.lst_math = []
        else:
            type_lst = [(i, type(i)) for i in lst]
            self.lst_math = [i[0] for i in type_lst if i[1] in (int, float)]

    def __add__(self, other):
        return ListMath([i + other for i in self.lst_math])

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        return ListMath([i - other for i in self.lst_math])

    def __rsub__(self, other):
        new = [other - i for i in self.lst_math]
        return ListMath(new)

    def __mul__(self, other):
        return ListMath([i * other for i in self.lst_math])

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        return ListMath([i / other for i in self.lst_math])

    def __rtruediv__(self, other):
        new = [other / i for i in self.lst_math]
        return ListMath(new)

    def __iadd__(self, other):
        self.lst_math = [i + other for i in self.lst_math]
        return self

    def __isub__(self, other):
        self.lst_math = [i - other for i in self.lst_math]
        return self

    def __imul__(self, other):
        self.lst_math = [i * other for i in self.lst_math]
        return self

    def __itruediv__(self, other):
        self.lst_math = [i / other for i in self.lst_math]
        return self


if __name__ == '__main__':
    lst = ListMath([1, "abc", -5, 7.68, True])
    lst = lst + 76  # сложение каждого числа списка с определенным числом
    lst += 76.7  # сложение каждого числа списка с определенным числом
    lst = lst - 76  # вычитание из каждого числа списка определенного числа
    lst = 7.0 - lst  # вычитание из числа каждого числа списка
    lst -= 76.3
    lst = lst * 5  # умножение каждого числа списка на указанное число (в данном случае на 5)
    lst = 5 * lst  # умножение каждого числа списка на указанное число (в данном случае на 5)
    lst *= 5.54
    lst = lst / 13  # деление каждого числа списка на указанное число (в данном случае на 13)
    lst /= 13.0
