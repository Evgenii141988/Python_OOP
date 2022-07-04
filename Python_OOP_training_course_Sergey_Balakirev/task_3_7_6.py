class Line:
    def __init__(self, x1: (int, float), y1: (int, float), x2: (int, float), y2: (int, float)):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __len__(self):
        return ((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) ** 0.5 >= 1


if __name__ == '__main__':
    line = Line(1, 2, 4, 5)
    print(bool(line))
