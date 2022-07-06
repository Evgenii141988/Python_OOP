class TriangleListIterator:
    def __init__(self, lst: list):
        self.lst = lst
        self.__len_lst = len(lst)

    # def __iter__(self):
    #     for i in range(self.__len_lst):
    #         for j in range(i + 1):
    #             yield self.lst[i][j]


    def __iter__(self):
        self.__res_lst = []
        for i in range(self.__len_lst):
            for j in range(i + 1):
                self.__res_lst.append(self.lst[i][j])
        self._index = -1
        return self

    def __next__(self):
        if self._index < len(self.__res_lst) - 1:
            self._index += 1
            return self.__res_lst[self._index]
        else:
            raise StopIteration


if __name__ == '__main__':
    lst = [['x00', 'x01', 'x02'],
           ['x10', 'x11'],
           ['x20', 'x21', 'x22', 'x23', 'x24'],
           ['x30', 'x31', 'x32', 'x33']]

    it = TriangleListIterator(lst)
    for x in it:  # последовательный перебор всех элементов списка: x00, x10, x11, x20, ...
        print(x)