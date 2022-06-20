class Bag:
    def __init__(self, max_weight: int):
        self.max_weight = max_weight
        self.__things = []

    @property
    def things(self):
        return self.__things

    def add_thing(self, thing: object):
        if self.get_total_weight() + thing.weight < self.max_weight:
            self.things.append(thing)

    def remove_thing(self, indx: int):
        self.things.pop(indx)

    def get_total_weight(self):
        return sum([thing.weight for thing in self.things])


class Thing:
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight


if __name__ == '__main__':
    bag = Bag(1000)
    bag.add_thing(Thing("Книга по Python", 100))
    bag.add_thing(Thing("Котелок", 500))
    bag.add_thing(Thing("Спички", 20))
    bag.add_thing(Thing("Бумага", 100))
    w = bag.get_total_weight()
    assert bag.get_total_weight() == 720
    for t in bag.things:
        print(f"{t.name}: {t.weight}")
