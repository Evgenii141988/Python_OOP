class InputDigits:
    def __init__(self, func):
        self.__func = func

    def __call__(self, *args, **kwargs):
        return [int(i) for i in self.__func().split()]


@InputDigits
def input_dg():
    return input()


if __name__ == '__main__':
    res = input_dg()
    print(res)
