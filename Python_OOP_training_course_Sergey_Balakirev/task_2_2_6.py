class StackObj:
    def __init__(self, data: str):
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value: str):
        self.__data = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj: object):
        if isinstance(obj, StackObj) or obj is None:
            self.__next = obj


class Stack:
    def __init__(self):
        self.top = None
        self.__end = None

    def push(self, obj: object):
        if self.top is None:
            self.top = obj
            self.__end = obj
        else:
            self.__end.next = obj
            self.__end = obj

    def pop(self):
        objs = []
        obj = self.top
        while obj:
            objs.append(obj)
            obj = obj.next
        try:
            obj = objs.pop()
            self.__end = objs[-1]
            self.__end.next = None
        except IndexError:
            self.top = None
            self.__end = None
        return obj

    def get_data(self):
        datas = []
        obj = self.top
        while obj:
            datas.append(obj.data)
            obj = obj.next
        return datas


if __name__ == '__main__':
    st = Stack()
    st.push(StackObj("obj1"))
    st.push(StackObj("obj2"))
    st.push(StackObj("obj3"))
    print(st.get_data())
    print(st.pop().data)
    print(st.pop().data)
    print(st.get_data())
    print(st._Stack__end.data)
    print(st.pop().data)
    print(st.top)
    print(st._Stack__end)
