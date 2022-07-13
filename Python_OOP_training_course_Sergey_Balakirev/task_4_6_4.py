class Digit:
    def __init__(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('значение не соответствует типу объекта')
        self.value = value


class Integer(Digit):
    def __init__(self, value):
        if not isinstance(value, int):
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(value)


class Float(Digit):
    def __init__(self, value):
        if not isinstance(value, float):
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(value)


class Positive(Digit):
    def __init__(self, value):
        if value < 0:
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(value)


class Negative(Digit):
    def __init__(self, value):
        if value >= 0:
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(value)


class PrimeNumber(Integer, Positive):
    def __init__(self, value):
        super().__init__(value)


class FloatPositive(Float, Positive):
    def __init__(self, value):
        super().__init__(value)


if __name__ == '__main__':
    digits = [PrimeNumber(3), PrimeNumber(5), PrimeNumber(7), FloatPositive(2.2), FloatPositive(3.3),
              FloatPositive(4.4), FloatPositive(5.5), FloatPositive(6.6)]
    lst_positive = list(filter(lambda x: isinstance(x, Positive), digits))
    lst_float = list(filter(lambda x: isinstance(x, Float), digits))
    print(lst_positive)
    print(lst_float)