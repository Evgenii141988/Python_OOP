class Clock:
    __DAY = 86400

    def __init__(self, seconds):
        if not isinstance(seconds, (int, float)):
            raise TypeError("Seconds must be int number")
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60
        m = self.seconds // 60 % 60
        h = self.seconds // 3600 % 24
        return f'{h:02}:{m:02}:{s:02}'

    @staticmethod
    def process(func):
        def inner(self, other):
            if not isinstance(other, (int, Clock)):
                raise ArithmeticError('Первый операнд должен быть int или Clock')

            sc = other
            if isinstance(other, Clock):
                sc = other.seconds

            return Clock(func(self.seconds, sc))

        return inner

    @process
    def __add__(self, other):
        return self + other

    @process
    def __sub__(self, other):
        return self - other

    @process
    def __mul__(self, other):
        return self * other

    @process
    def __truediv__(self, other):
        return self / other

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        print('__iadd__')
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('Первый операнд должен быть int или Clock')

        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
        self.seconds += sc
        return self

    def __eq__(self, other):
        sc = other if isinstance(other, int) else other.seconds
        return self.seconds == sc

    def __lt__(self, other):
        sc = other if isinstance(other, int) else other.seconds
        return self.seconds < sc

    def __gt__(self, other):
        sc = other if isinstance(other, int) else other.seconds
        return self.seconds < sc

if __name__ == '__main__':
    c1 = Clock(1000)
    c2 = Clock(2000)
    c3 = c1 / c2
    # c1 = 1000 + c1
    # c1 += 100
    # print(c3.get_time())
    print(1000 == c1)
    print(1000 > c1)
    print(1000 < c1)
