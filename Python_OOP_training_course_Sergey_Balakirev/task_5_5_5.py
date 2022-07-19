class Box:
    def __init__(self, name: str, max_weight: (int, float)):
        self._name = name
        self._max_weight = max_weight
        self._real_weight = 0
        self._things = []

    def add_thing(self, obj: tuple):
        name, weight = obj
        if self._real_weight + weight > self._max_weight:
            raise ValueError('превышен суммарный вес вещей')
        self._things.append(obj)
        self._real_weight += weight

    @property
    def things(self):
        return self._things

    @things.setter
    def things(self, lst: list):
        self._things = lst


class BoxDefender:
    def __init__(self, box: Box):
        self._box = box
        self._things = box.things[:]

    def __enter__(self):
        return self._box

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self._box.things = self._things
        return False

if __name__ == '__main__':
    b = Box('name', 2000)
    assert b._name == 'name' and b._max_weight == 2000, "неверные значения атрибутов объекта класса Box"

    b.add_thing(("1", 100))
    b.add_thing(("2", 200))

    try:
        with BoxDefender(b) as bb:
            bb.add_thing(("3", 1000))
            bb.add_thing(("4", 1900))
    except ValueError:
        assert len(b._things) == 2

    else:
        assert False, "не сгенерировалось исключение ValueError"

