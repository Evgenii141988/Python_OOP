class Point:
    def __init__(self, x: (int, float) = 0, y: (int, float) = 0):
        self._x = x
        self._y = y


if __name__ == '__main__':
    a, b = input().split()
    try:
        a = int(a)
        b = int(b)
        pt = Point(a, b)
    except:
        try:
            a = float(a)
            b = float(b)
            pt = Point(a, b)
        except:
            pt = Point()
    finally:
        print(f'Point: x = {pt._x}, y = {pt._y}')
