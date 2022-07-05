class Array:
    def __init__(self, max_length: int, cell: object):
        self.max_length = max_length
        self.cell = cell
        self.__array = [self.cell() for _ in range(max_length)]

    def check_indx(self, indx: int):
        if not (isinstance(indx, int) and 0 <= indx < self.max_length):
            raise IndexError('неверный индекс для доступа к элементам массива')

    def __getitem__(self, item: int):
        self.check_indx(item)
        return self.__array[item].value

    def __setitem__(self, key: int, value):
        self.check_indx(key)
        self.__array[key].value = value

    def __str__(self):
        return ' '.join([str(cell.value) for cell in self.__array])


class Integer:
    def __init__(self, start_value=0):
        self.__value = start_value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        if not isinstance(value, int):
            raise ValueError('должно быть целое число')
        self.__value = value


if __name__ == '__main__':
    ar_int = Array(10, cell=Integer)
    print(ar_int[3])
    print(ar_int)  # должны отображаться все значения массива в одну строчку через пробел
    ar_int[1] = 10
    print(ar_int)
    # ar_int[1] = 10.5  # должно генерироваться исключение ValueError
    ar_int[10] = 1  # должно генерироваться исключение IndexError
