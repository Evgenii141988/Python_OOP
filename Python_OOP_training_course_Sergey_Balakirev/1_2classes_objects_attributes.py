class Point:
    '''Класс для представления координат точек на плоскости'''
    color = 'red'
    circle = 2


if __name__ == '__main__':
    Point.color = 'black'
    a = Point()
    b = Point()
    a.x = 1
    a.y = 2
    b.x = 10
    b.y = 20