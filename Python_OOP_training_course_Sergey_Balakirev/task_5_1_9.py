class Triangle:
    def __init__(self, a: (int, float), b: (int, float), c: (int, float)):
        self._a = a
        self._b = b
        self._c = c
        self.__check_triangle()

    def __setattr__(self, key: str, value: (int, float)):
        if not (isinstance(value, (int, float)) and value > 0):
            raise TypeError('стороны треугольника должны быть положительными числами')
        super().__setattr__(key, value)

    def __check_triangle(self):
        if not (self._a < self._c + self._b and self._c < self._a + self._b and self._b < self._c + self._a):
            raise ValueError('из указанных длин сторон нельзя составить треугольник')


if __name__ == '__main__':
    input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5), (7, 4, 6)]
    lst_tr = []
    for elm in input_data:
        try:
            lst_tr.append(Triangle(*elm))
        except:
            continue
    print(lst_tr)