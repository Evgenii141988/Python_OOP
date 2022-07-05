class Record:
    def __init__(self, **kwargs):
        self.__dict__ = kwargs

    def get_key(self, item: int):
        return list(self.__dict__)[item]

    def check_item(self, item):
        if not (isinstance(item, int) and 0 <= item < len(self.__dict__)):
            raise IndexError('неверный индекс поля')

    def __getitem__(self, item: int):
        self.check_item(item)
        return self.__dict__[self.get_key(item)]

    def __setitem__(self, key: int, value):
        self.check_item(key)
        self.__dict__[self.get_key(key)] = value


if __name__ == '__main__':
    r = Record(pk=1, title='Python ООП', author='Балакирев')
    r[0] = 2  # доступ к полю pk
    r[1] = 'Супер курс по ООП'  # доступ к полю title
    r[2] = 'Балакирев С.М.'  # доступ к полю author
    print(r[1])  # Супер курс по ООП
    r[3]  # генерируется исключение IndexError
