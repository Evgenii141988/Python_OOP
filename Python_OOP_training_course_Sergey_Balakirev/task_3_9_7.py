class IterColumn:
    def __init__(self, lst: list, column: int):
        self.lst = lst
        self.column = column

    def __iter__(self):
        for i in range(len(self.lst)):
            yield self.lst[i][self.column]

if __name__ == '__main__':
    lst = [['x00', 'x01', 'x02'],
           ['x10', 'x11', 'x12'],
           ['x20', 'x21', 'x22'],
           ['x30', 'x31', 'x32']]

    it = IterColumn(lst, 0)
    for x in it:  # последовательный перебор всех элементов столбца списка: x12, x22, ..., xM2
        print(x)