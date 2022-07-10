class SoftList(list):
    def __setitem__(self, key, value):
        try:
            super().__setitem__(key, value)
        except IndexError:
            return False

    def __getitem__(self, item):
        try:
            return super().__getitem__(item)
        except IndexError:
            return False


if __name__ == '__main__':
    sl = SoftList("python")
    print(sl[0])
    print(sl[-1])
    print(sl[6])
    print(sl[-7])