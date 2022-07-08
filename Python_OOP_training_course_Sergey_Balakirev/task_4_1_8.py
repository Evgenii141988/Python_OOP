class Validator:

    def _is_valid(self, data):
        return True

    def __call__(self, data):
        if not self._is_valid(data):
            raise ValueError('данные не прошли валидацию')
        return self._is_valid(data)


class IntegerValidator(Validator):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data: int):
        return isinstance(data, int) and self.min_value <= data <= self.max_value


class FloatValidator(Validator):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data: float):
        return isinstance(data, float) and self.min_value <= data <= self.max_value


if __name__ == '__main__':
    integer_validator = IntegerValidator(-10, 10)
    float_validator = FloatValidator(-1, 1)
    res1 = integer_validator(-10)  # True
    res2 = float_validator(-1.0)  # исключение ValueError
    print(res1)
    print(res2)