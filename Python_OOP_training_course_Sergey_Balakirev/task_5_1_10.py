class Validator:
    def __init__(self, min_value: (int, float), max_value: (int, float)):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value: (int, float)):
        if isinstance(self, FloatValidator):
            if not (type(value) == float and self.min_value <= value <= self.max_value):
                raise ValueError('значение не прошло валидацию')
        if isinstance(self, IntegerValidator):
            if not (type(value) == int and self.min_value <= value <= self.max_value):
                raise ValueError('значение не прошло валидацию')


class FloatValidator(Validator):
    def __init__(self, min_value: (int, float), max_value: (int, float)):
        super().__init__(min_value, max_value)


class IntegerValidator(Validator):
    def __init__(self, min_value: (int, float), max_value: (int, float)):
        super().__init__(min_value, max_value)


def is_valid(lst: list, validators: list):
    result = []
    for elm in lst:
        for validator in validators:
            try:
                validator(elm)
                result.append(elm)
                break
            except ValueError:
                continue
    return result


if __name__ == '__main__':
    fv = FloatValidator(0, 10.5)
    iv = IntegerValidator(-10, 20)
    lst_out = is_valid([1, 4.5, -10.5, 100, True, 'abc', (1, 2)], validators=[fv, iv])  # [1, 4.5]
    print(lst_out)
