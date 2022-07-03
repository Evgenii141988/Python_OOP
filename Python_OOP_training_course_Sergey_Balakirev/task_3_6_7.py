import sys


class DataBase:
    def __init__(self, path: str):
        self.path = path
        self.dict_db = {}

    def write(self, record: object):
        self.dict_db[record] = self.dict_db.get(record, []) + [record]

    def read(self, pk: int):
        for value in self.dict_db.values():
            for obj in value:
                if pk == obj.pk:
                    return obj


class Record:
    UNIQUE_RECORD_IDENTIFIER = 0

    def __init__(self, fio: str, descr: str, old: int):
        Record.UNIQUE_RECORD_IDENTIFIER += 1
        self.fio = fio
        self.descr = descr
        self.old = old
        self.pk = Record.UNIQUE_RECORD_IDENTIFIER

    def __hash__(self):
        return hash((self.fio.lower(), self.old))

    def __eq__(self, other: object):
        if not isinstance(other, Record):
            raise TypeError('Объекты сравнения должны иметь тип Record')
        return hash(self) == hash(other)


if __name__ == '__main__':
    lst_in = list(map(str.strip, sys.stdin.readlines()))
    db = DataBase('path')
    for string in lst_in:
        fio, descr, old = string.split('; ')
        db.write(Record(fio, descr, old))
    print(db.dict_db)
    print(db.read(4).fio)