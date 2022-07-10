class Thing:
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight


class ArtObject(Thing):
    def __init__(self, name: str, weight: float, author: str, date: str):
        super().__init__(name, weight)
        self.author = author
        self.date = date


class Computer(Thing):
    def __init__(self, name: str, weight: float, memory: int, CPU: str):
        super().__init__(name, weight)
        self.memory = memory
        self.CPU = CPU


class Auto(Thing):
    def __init__(self, name: str, weight: float, dims: tuple, model: str):
        super().__init__(name, weight)
        self.dims = dims
        self.model = model


class Mercedes(Auto):
    def __init__(self, name: str, weight: float, dims: tuple, model: str, old: int):
        super().__init__(name, weight, dims, model)
        self.old = old


class Toyota(Auto):
    def __init__(self, name: str, weight: float, dims: tuple, model: str, wheel: bool):
        super().__init__(name, weight, dims, model)
        self.wheel = wheel


if __name__ == '__main__':
    s_class = Mercedes('Mercedes', 2500, (100, 5000, 100), 's500', 3)
    print(s_class.__dict__)