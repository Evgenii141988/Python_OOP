class Box:
    def __init__(self):
        self.__box = []

    def add_thing(self, obj: object):
        self.__box.append(obj)

    def get_things(self):
        return self.__box

    def __eq__(self, other: object):
        for obj in self.get_things():
            if obj not in other.get_things():
                return False
        return True


class Thing:
    def __init__(self, name: str, mass: (int, float)):
        self.name = name
        self.mass = mass

    def __eq__(self, other: object):
        return self.name.lower() == other.name.lower() and self.mass == other.mass


if __name__ == '__main__':
    b1 = Box()
    b2 = Box()

    b1.add_thing(Thing('мел', 100))
    b1.add_thing(Thing('тряпка', 200))
    b1.add_thing(Thing('доска', 2000))

    b2.add_thing(Thing('тряпка', 200))
    b2.add_thing(Thing('мел', 100))
    b2.add_thing(Thing('доска', 2000))


    res = b1 == b2  # True
    print(res)
