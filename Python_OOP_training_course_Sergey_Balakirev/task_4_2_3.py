class ListInteger(list):
    def __init__(self, lst):
        if not all((isinstance(i, int) for i in lst)):
            raise TypeError('можно передавать только целочисленные значения')
        super().__init__(lst)

    def __setitem__(self, key: int, value: int):
        if not isinstance(value, int):
            raise TypeError('можно передавать только целочисленные значения')
        super().__setitem__(key, value)

    def append(self, value: int):
        if not isinstance(value, int):
            raise TypeError('можно передавать только целочисленные значения')
        super().append(value)


if __name__ == '__main__':
    s = ListInteger((1, 2, 3))
    s[1] = 10
    s.append(11)
    print(s)
    s[0] = 10.5  # TypeError
