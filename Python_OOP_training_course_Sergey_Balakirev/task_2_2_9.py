from math import sqrt


class PathLines:
    def __init__(self, *args):
        self.lines = list(args)

    def get_path(self):
        return self.lines

    def get_length(self):
        x = y = 0
        L = 0
        if self.lines:
            for line in self.lines:
                L += sqrt((line.x - x) ** 2 + (line.y - y) ** 2)
                x = line.x
                y = line.y
        return L

    def add_line(self, line: object):
        self.lines.append(line)


class LineTo:
    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == '__main__':
    p = PathLines(LineTo(10, 20), LineTo(10, 30))
    p.add_line(LineTo(20, -10))
    dist = p.get_length()
    print(dist)