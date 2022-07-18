class TupleData:
    def __init__(self, *args):
        self.cells = list(args)

    def __getitem__(self, item: int):
        self.check_index(item)
        return self.cells[item].value

    def __setitem__(self, key: int, value):
        self.check_index(key)
        self.cells[key].value = value

    def check_index(self, index: int):
        if not (isinstance(index, int) and 0 <= index < len(self.cells)):
            raise IndexError(f'Индекс должен быть целым числом в диапазоне от 0 до {len(self.cells) - 1}')

    def __len__(self):
        return len(self.cells)

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if self.__index < len(self.cells):
            index = self.__index
            self.__index += 1
            return self.cells[index].value
        else:
            raise StopIteration


class Cell:
    def __init__(self, min_value: (int, float), max_value: (int, float)):
        if isinstance(self, CellString):
            self._min_length = min_value
            self._max_length = max_value
        else:
            self._min_value = min_value
            self._max_value = max_value
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, val):
        if isinstance(self, CellInteger) and not self._min_value <= val <= self._max_value:
            raise CellIntegerException('значение выходит за допустимый диапазон')
        if isinstance(self, CellFloat) and not self._min_value <= val <= self._max_value:
            raise CellFloatException('значение выходит за допустимый диапазон')
        if isinstance(self, CellString) and not self._min_length <= len(val) <= self._max_length:
            raise CellStringException('длина строки выходит за допустимый диапазон')
        self.__value = val


class CellInteger(Cell):
    def __init__(self, min_value: (int, float), max_value: (int, float)):
        super().__init__(min_value, max_value)


class CellFloat(Cell):
    def __init__(self, min_value: (int, float), max_value: (int, float)):
        super().__init__(min_value, max_value)


class CellString(Cell):
    def __init__(self, min_length: int, max_length: int):
        super().__init__(min_length, max_length)


class CellException(Exception):
    def __init__(self, message: str = ''):
        self.message = message

    def __str__(self):
        return self.message


class CellIntegerException(CellException):
    def __init__(self, message: str):
        super().__init__(message)


class CellFloatException(CellException):
    def __init__(self, message: str):
        super().__init__(message)


class CellStringException(CellException):
    def __init__(self, message: str):
        super().__init__(message)


if __name__ == '__main__':
    ld = TupleData(CellInteger(0, 10), CellInteger(11, 20), CellFloat(-10, 10), CellString(1, 100))

    try:
        ld[44] = 1
        ld[1] = 20
        ld[2] = -5.6
        ld[3] = "Python ООП"
    except CellIntegerException as e:
        print(e)
    except CellFloatException as e:
        print(e)
    except CellStringException as e:
        print(e)
    except CellException:
        print("Ошибка при обращении к ячейке")
    except Exception:
        print("Общая ошибка при работе с объектом TupleData")
    #
    # res = len(ld)  # возвращает общее число элементов (ячеек) в объекте ld
    # print(res)
    # for d in ld:  # перебирает значения ячеек объекта ld (значения, а не объекты ячеек)
    #     print(d)

    # t = TupleData(CellInteger(-10, 10), CellInteger(0, 2), CellString(5, 10))
    #
    # d = (1, 0, 'sergey')
    # t[0] = d[0]
    # t[1] = d[1]
    # t[2] = d[2]
    # for i, x in enumerate(t):
    #     assert x == d[i], "объект класса TupleData хранит неверную информацию"
    #
    # assert len(t) == 3, "неверное число элементов в объекте класса TupleData"
    #
    # cell = CellFloat(-5, 5)
    # try:
    #     cell.value = -6.0
    # except CellFloatException:
    #     assert True
    # else:
    #     assert False, "не сгенерировалось исключение CellFloatException"
    #
    # cell = CellInteger(-1, 7)
    # try:
    #     cell.value = 8
    # except CellIntegerException:
    #     assert True
    # else:
    #     assert False, "не сгенерировалось исключение CellIntegerException"
    #
    # cell = CellString(5, 7)
    # try:
    #     cell.value = "hello world"
    # except CellStringException:
    #     assert True
    # else:
    #     assert False, "не сгенерировалось исключение CellStringException"
    #
    # assert issubclass(CellIntegerException, CellException) and issubclass(CellFloatException,
    #                                                                       CellException) and issubclass(
    #     CellStringException,
    #     CellException), "классы CellIntegerException, CellFloatException, CellStringException должны наследоваться от класса CellException"
