class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y


if __name__ == '__main__':
    pt = Point(1, 2)
    try:
        pt.z
    except AttributeError:
        print("Атрибут с именем z не существует")
