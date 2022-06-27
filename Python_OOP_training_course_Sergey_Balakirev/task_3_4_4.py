class NewList:
    def __init__(self, lst: list = None):
        self.lst = [] if lst is None else lst

    def get_list(self):
        return self.lst

    @classmethod
    def __get_new_list(cls, lst1, lst2):
        d1 = [(i, type(i)) for i in lst1]
        d2 = [(i, type(i)) for i in lst2]
        for i in d2:
            if i in d1:
                d1.remove(i)
        return [i[0] for i in d1]

    def __sub__(self, other):
        if not isinstance(other, (list, NewList)):
            raise ArithmeticError("Операторы должны быть list или NewList")

        second_lst = other
        if isinstance(other, NewList):
            second_lst = other.lst
        return NewList(self.__get_new_list(self.lst, second_lst))

    def __rsub__(self, other):
        new_obj = NewList(other)
        return new_obj - self

    def __isub__(self, other):
        if not isinstance(other, (list, NewList)):
            raise ArithmeticError("Операторы должны быть list или NewList")

        second_lst = other
        if isinstance(other, NewList):
            second_lst = other.lst

        self.lst = self.__get_new_list(self.lst, second_lst)
        return self


if __name__ == '__main__':
    lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
    lst2 = NewList([0, 1, 2, 3, True])
    res_1 = lst1 - lst2  # NewList: [-4, 6, 10, 11, 15, False]
    print(res_1.get_list())
    lst1 -= lst2  # NewList: [-4, 6, 10, 11, 15, False]
    print(lst1.get_list())
    res_2 = lst2 - [0, True]  # NewList: [1, 2, 3]
    print(res_2.get_list())
    res_3 = [1, 2, 3, 4.5] - res_2  # NewList: [4.5]
    print(f'res_2{res_2.get_list()}')
    print(res_3.get_list())
    a = NewList([2, 3])
    res_4 = [1, 2, 2, 3] - a  # NewList: [1, 2]
    print(res_4.get_list())

