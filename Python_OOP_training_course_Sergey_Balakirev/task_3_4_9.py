class Box3D:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def __add__(self, other: object):
        return Box3D(self.width + other.width, self.height + other.height, self.depth + other.depth)

    def __mul__(self, other: (int, float)):
        return Box3D(self.width * other, self.height * other, self.depth * other)

    def __rmul__(self, other: (int, float)):
        return self * other

    def __sub__(self, other: object):
        return Box3D(self.width - other.width, self.height - other.height, self.depth - other.depth)

    def __floordiv__(self, other: int):
        return Box3D(self.width // other, self.height // other, self.depth // other)

    def __mod__(self, other: int):
        return Box3D(self.width % other, self.height % other, self.depth % other)


if __name__ == '__main__':
    box1 = Box3D(1, 2, 3)
    box2 = Box3D(2, 4, 6)
    box3 = box1 + box2  # Box3D: width=3, height=6, depth=9 (соответствующие размерности складываются)
    box4 = box1 * 2  # Box3D: width=2, height=4, depth=6 (каждая размерность умножается на 2)
    box5 = 3 * box2  # Box3D: width=6, height=12, depth=18
    box6 = box2 - box1  # Box3D: width=1, height=2, depth=3 (соответствующие размерности вычитаются)
    box7 = box1 // 2  # Box3D: width=0, height=1, depth=1 (соответствующие размерности целочисленно делятся на 2)
    box8 = box2 % 3  # Box3D: width=2, height=1, depth=0
    print(box3.width, box3.height, box3.depth)
    print(box4.width, box4.height, box4.depth)
    print(box5.width, box5.height, box5.depth)
    print(box6.width, box6.height, box6.depth)
    print(box7.width, box7.height, box7.depth)
    print(box8.width, box8.height, box8.depth)
