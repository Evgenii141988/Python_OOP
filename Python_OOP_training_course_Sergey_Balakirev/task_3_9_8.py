class Stack:
    def __init__(self):
        self.top = None
        self.__obj_list = []

    def push_back(self, obj: object):
        if self.top is None:
            self.top = obj
        else:
            self.__obj_list[-1].next = obj
        self.__obj_list.append(obj)

    def push_front(self, obj: object):
        obj.next = self.__obj_list[0]
        self.top = obj
        self.__obj_list.insert(0, obj)

    def check_index(self, index: int):
        if not (isinstance(index, int) and 0 <= index <= len(self.__obj_list) - 1):
            raise IndexError('неверный индекс')

    def __len__(self):
        return len(self.__obj_list)

    def __getitem__(self, item: int):
        self.check_index(item)
        return self.__obj_list[item].data

    def __setitem__(self, key: int, value):
        self.check_index(key)
        self.__obj_list[key].data = value

    def __iter__(self):
        return (obj for obj in self.__obj_list)


class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None


if __name__ == '__main__':
    s = Stack()
    s.push_back(StackObj('1'))
    s.push_front(StackObj('2'))
    s.push_front(StackObj('3'))
    s.push_back(StackObj('4'))
    s[0] = '55'
    print(s[0])
    for obj in s:  # перебор объектов стека (с начала и до конца)
        print(obj.data)