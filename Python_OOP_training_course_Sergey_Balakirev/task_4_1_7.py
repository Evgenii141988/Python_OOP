class Singleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name: str):
        self.name = name


class Game(Singleton):

    def __init__(self, name: str):
        if not hasattr(self, 'name'):
            super().__init__(name)


if __name__ == '__main__':
    g1 = Game('111')
    g2 = Game('222')
    print(g1)
    print(g2)
    print(g1.name)
    print(g2.name)
