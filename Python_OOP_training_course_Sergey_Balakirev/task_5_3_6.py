class TupleLimit(tuple):
    def __new__(cls, lst, max_length):
        return super().__new__(cls, tuple(lst))

    def __init__(self, lst: (list, tuple), max_length: int):
        if len(lst) > max_length:
            raise ValueError('число элементов коллекции превышает заданный предел')
        self.lst = list(lst)
        self.max_length = max_length

    def __str__(self):
        return ' '.join(str(i) for i in self.lst)

    def __repr__(self):
        return ' '.join(str(i) for i in self.lst)


if __name__ == '__main__':
    digits = list(map(float, input().split()))
    try:
        tl = TupleLimit(digits, 5)
        print(tl)
    except ValueError as v:
        print(v)

