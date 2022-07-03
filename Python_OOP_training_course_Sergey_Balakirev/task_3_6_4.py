class Rect:
    def __init__(self, x: (int, float), y: (int, float), width: (int, float), height: (int, float)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __hash__(self):
        return hash((self.width, self.height))


if __name__ == '__main__':
    r1 = Rect(10, 5, 100, 50)
    r2 = Rect(-10, 4, 100, 50)

    h1, h2 = hash(r1), hash(r2)  # h1 == h2
    print(h1)
    print(h2)
