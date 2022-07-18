class StringException(Exception):
    pass


class NegativeLengthString(Exception):
    """ошибка, если длина отрицательная"""


class ExceedLengthString(Exception):
    """ошибка, если длина превышает заданное значение"""


if __name__ == '__main__':
    try:
        raise ExceedLengthString
    except NegativeLengthString:
        print("NegativeLengthString")
    except ExceedLengthString:
        print("ExceedLengthString")
    except StringException:
        print("StringException")
