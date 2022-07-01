class Body:
    def __init__(self, name: str, ro: (int, float), volume: (int, float)):
        self.name = name
        self.ro = ro
        self.volume = volume

    @classmethod
    def check_value(cls, value):
        if not isinstance(value, (int, float, Body)):
            raise TypeError('Неверный тип значения')
        vl = value.volume * value.ro if isinstance(value, Body) else value
        return vl

    def __eq__(self, other):
        value = self.check_value(other)
        return self.ro * self.volume == value

    def __lt__(self, other):
        value = self.check_value(other)
        return self.ro * self.volume < value


if __name__ == '__main__':
    body1 = Body('cube', 10, 20)
    body2 = Body('rec', 20, 30)
    print(body1 > body2)
    print(body1 != body2)
    print(body1 < 10)
    print(body2 == 5)
