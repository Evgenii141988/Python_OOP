class WordString:
    def __init__(self, string=''):
        self.__string = string

    @property
    def string(self):
        return self.__string

    @string.setter
    def string(self, value):
        self.__string = value

    def __len__(self):
        return len(self.string.split())

    def __call__(self, indx: int, *args, **kwargs):
        return self.string.split()[indx]


if __name__ == '__main__':
    words = WordString()
    words.string = "Курс по Python ООП"
    n = len(words)
    first = "" if n == 0 else words(0)
    print(words.string)
    print(f"Число слов: {n}; первое слово: {first}")
