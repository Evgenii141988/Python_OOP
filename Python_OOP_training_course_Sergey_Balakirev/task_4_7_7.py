class Note:
    def __init__(self, name: str, ton: int):
        self._name = name
        self._ton = ton

    def __setattr__(self, key, value):
        if key == '_name' and value not in ('до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си'):
            raise ValueError('недопустимое значение аргумента')
        if key == '_ton' and value not in (-1, 0, 1):
            raise ValueError('недопустимое значение аргумента')
        super().__setattr__(key, value)


class Notes:
    __slots__ = ('_do', '_re', '_mi', '_fa', '_solt', '_la', '_si')
    __alone = None
    __notes = ('до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си')

    def __new__(cls, *args, **kwargs):
        if cls.__alone is None:
            cls.__alone = object.__new__(cls)
        return cls.__alone

    def __init__(self):
        for i in range(len(self.__notes)):
            setattr(self, self.__slots__[i], Note(self.__notes[i], 0))

    def _check_index(self, index: int):
        if not (isinstance(index, int) and 0 <= index <= 6):
            raise IndexError('недопустимый индекс')

    def __getitem__(self, item: int):
        self._check_index(item)
        return getattr(self, self.__slots__[item])


if __name__ == '__main__':
    notes = Notes()
    nota = notes[2]  # ссылка на ноту ми
    notes[3]._ton = -1  # изменение тональности ноты фа
    print(nota.__dict__)
    print(nota)
    print(notes[3]._ton)