class Dimensions:
    def __init__(self, a: (int, float), b: (int, float), c: (int, float)):
        self.a = a
        self.b = b
        self.c = c

    def __setattr__(self, key, value):
        if value <= 0:
            raise ValueError("габаритные размеры должны быть положительными числами")
        super().__setattr__(key, value)

    def __hash__(self):
        return hash((self.a, self.b, self.c))


def get_int_or_float_number(string: str) -> (int, float):
    return int(string) if string.isdigit() else float(string)


if __name__ == '__main__':
    s_inp = input()
    lst_dims = []
    for nums in s_inp.split('; '):
        a, b, c = [get_int_or_float_number(num) for num in nums.split()]
        lst_dims.append(Dimensions(a, b, c))
    lst_dims.sort(key=hash)
