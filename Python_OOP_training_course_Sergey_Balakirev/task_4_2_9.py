class IteratorAttrs:
    def __init__(self, model: str, size: tuple, memory: int):
        self.model = model
        self.size = size
        self.memory = memory

    def __iter__(self):
        self.keys = list(self.__dict__)
        self.indx = 0
        return self

    def __next__(self):
        if self.indx < len(self.keys):
            key = self.keys[self.indx]
            self.indx += 1
            return key, self.__dict__[key]
        else:
            raise StopIteration


class SmartPhone(IteratorAttrs):
    def __init__(self, model: str, size: tuple, memory: int):
        super().__init__(model, size, memory)


if __name__ == '__main__':
    phone = SmartPhone('Samsung', (1, 2), 512)
    for attr, value in phone:
        print(attr, value)
