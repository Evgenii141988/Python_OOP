class Point:
    '''Класс для представления координат точек на плоскости'''
    color = 'red'
    circle = 2

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y


if __name__ == '__main__':
    Point.color = 'black'
    a = Point()
    b = Point()
    a.x = 1
    a.y = 2
    b.x = 10
    b.y = 20
    pt = Point()
    pt.set_coords(1, 3)
    print(pt.__dict__)
    print(pt.get_coords())