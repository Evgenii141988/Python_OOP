class Money:
    type_money = None
    CURRENCY_EXCHANGE_RATE_ERROR = 0.1

    def __init__(self, volume: (int, float) = 0):
        self.__cb = None
        self.__volume = volume

    def get_money_values(self, other: object):
        if self.cb is None:
            raise ValueError("Неизвестен курс валют.")

        value_1 = self.volume / self.cb.rates[self.type_money]
        value_2 = other.volume / other.cb.rates[other.type_money]
        return value_1, value_2

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, value):
        self.__cb = value

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, value):
        self.__volume = value

    def __eq__(self, other):
        value1, value2 = self.get_money_values(other)
        return abs(value1 - value2) < self.CURRENCY_EXCHANGE_RATE_ERROR

    def __le__(self, other):
        value1, value2 = self.get_money_values(other)
        return value1 <= value2

    def __lt__(self, other):
        value1, value2 = self.get_money_values(other)
        return value1 < value2


class MoneyR(Money):  # для рублевых кошельков
    type_money = 'rub'


class MoneyD(Money):  # для долларовых кошельков
    type_money = 'dollar'


class MoneyE(Money):  # для евро-кошельков
    type_money = 'euro'


class CentralBank:
    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    def __new__(cls):
        return None

    @classmethod
    def register(cls, money: object):
        money.cb = cls


if __name__ == '__main__':
    CentralBank.rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    r = MoneyR(45000)
    d = MoneyD(500)

    CentralBank.register(r)
    CentralBank.register(d)

    if r > d:
        print("неплохо")
    else:
        print("нужно поднажать")
