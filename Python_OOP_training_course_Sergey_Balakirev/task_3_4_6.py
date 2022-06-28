class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value


class Stack:
    def __init__(self):
        self.top = None

    def push_back(self, obj: object):
        """Добавление объекта класса StackObj в конец односвязного списка"""
        if self.top is None:
            self.top = obj
        else:
            obj_box = self.top
            while True:
                if obj_box.next is None:
                    obj_box.next = obj
                    break
                obj_box = obj_box.next

    def pop_back(self):
        """Удаление последнего объекта из односвязного списка"""
        obj = self.top
        while True:
            try:
                if obj.next.next is None:
                    obj.next = None
                    break
                obj = obj.next
            except AttributeError:
                self.top = None
                break

    def __add__(self, other: object):
        """Operation + """
        self.push_back(other)
        return self

    def __iadd__(self, other: object):
        """Operation =+ """
        return self + other

    def __mul__(self, other: list):
        """Operation * """
        for data in other:
            self.push_back(StackObj(data))
        return self

    def __imul__(self, other: list):
        """Operation =* """
        return self * other


if __name__ == '__main__':
    st = Stack()
    st.push_back(StackObj('1'))
    st.push_back(StackObj('2'))
    st.push_back(StackObj('3'))
    st = st + StackObj('4')
    st += StackObj('5')
    st = st * ['6', '7', '8']
    st *= ['9', '10', '11']
    st.pop_back()
    st.pop_back()
    st.pop_back()
    st.pop_back()
    print(st.top)
    print(st)

