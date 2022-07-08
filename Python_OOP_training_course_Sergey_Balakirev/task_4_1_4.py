class Animal:
    def __init__(self, name: str, old: int):
        self.name = name
        self.old = old


class Cat(Animal):
    def __init__(self, name: str, old: int, color: str, weight: (int, float)):
        super().__init__(name, old)
        self.color = color
        self.weight = weight

    def get_info(self):
        return f'{self.name}: {self.old}, {self.color}, {self.weight}'


class Dog(Animal):
    def __init__(self, name: str, old: int, breed: str, size: tuple):
        super().__init__(name, old)
        self.breed = breed
        self.size = size

    def get_info(self):
        return f'{self.name}: {self.old}, {self.breed}, {self.size}'


if __name__ == '__main__':
    cat = Cat('кот', 4, 'black', 2.25)
    dog = Dog('пес', 3, 'red', (2, 3))
    print(cat.get_info())
    print(dog.get_info())
