class StringException(Exception):
    pass


class NegativeLengthString(Exception):
    pass


class ExceedLengthString(Exception):
    pass


if __name__ == '__main__':
    try:
        raise ExceedLengthString
    except NegativeLengthString:
        print("NegativeLengthString")
    except ExceedLengthString:
        print("ExceedLengthString")
    except StringException:
        print("StringException")
