def get_method(func, lst):
    def wrapper(*args):
        lst.append(func.__name__)
        return func(*args)

    return wrapper


def class_log(lst: list):
    def wrapper(cls):
        methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
        for k, v in methods.items():
            setattr(cls, k, get_method(v, lst))

        return cls

    return wrapper


vector_log = []  # наименование (vector_log) в программе не менять!


@class_log(vector_log)
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value

    def get_coords(self):
        return self.__coords

if __name__ == '__main__':
    v = Vector(1, 2, 3)
    v[0] = 10
    print(v[0])
    print(v[0])
    print(v[0])
    # print(v.get_coords())
    print(vector_log)