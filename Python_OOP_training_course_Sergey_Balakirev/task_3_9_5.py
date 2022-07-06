class Person:
    def __init__(self, fio: str, job: str, old: int, salary: (int, float), year_job: int):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job
        self.__data = list(self.__dict__)

    def __check_index(self, index: int):
        if not (isinstance(index, int) and 0 <= index <= 4):
            raise IndexError('неверный индекс')

    def __iter__(self):
        self._index = -1
        return self

    def __next__(self):
        if self._index < 4:
            self._index += 1
            return getattr(self, self.__data[self._index])
        raise StopIteration

    def __getitem__(self, item: int):
        self.__check_index(item)
        key = self.__data[item]
        return getattr(self, key)

    def __setitem__(self, key: int, value):
        self.__check_index(key)
        key = self.__data[key]
        setattr(self, key, value)


if __name__ == '__main__':
    pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
    pers[0] = 'Балакирев С.М.'
    # print(pers.fio)
    for v in pers:
        print(v)
    # pers[5] = 123  # IndexError
