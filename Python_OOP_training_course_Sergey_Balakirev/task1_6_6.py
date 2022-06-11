class Factory:
    @staticmethod
    def build_sequence():
        return []

    @staticmethod
    def build_number(string):
        try:
            return int(string)
        except ValueError:
            print(f'Невозможно преобразовать значение {string} в целое число')


class Loader:
    @staticmethod
    def parse_format(string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq


if __name__ == '__main__':
    # эти строчки не менять!
    res = Loader.parse_format("1, 2, 3, -5, 10", Factory)
    print(res)
