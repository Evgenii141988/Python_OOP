class StackObj:
    def __init__(self, data: str):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.__counter = 0

    def push(self, obj: object):
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
        self.__counter += 1

    def pop(self):
        """извлечение последнего объекта с его удалением из стека"""
        obj = self.top
        while True:
            try:
                if obj.next.next is None:
                    del_obj = obj.next
                    obj.next = None
                    self.__counter -= 1
                    return del_obj
                obj = obj.next
            except AttributeError:
                del_obj = self.top
                self.top = None
                self.__counter = 0
                return del_obj

    def get_obj(self, indx: int):
        """получение объеката по индексу"""
        i = 0
        obj = self.top
        while i < indx:
            i += 1
            obj = obj.next
        return obj

    def check_indx(self, indx: int):
        if not (isinstance(indx, int) and 0 <= indx < self.__counter):
            raise IndexError('неверный индекс')

    def __getitem__(self, item: int):
        self.check_indx(item)
        return self.get_obj(item)

    def __setitem__(self, key: int, value: object):
        self.check_indx(key)
        prev_obj = self.get_obj(key - 1)
        next_obj = self.get_obj(key + 1)
        obj = self.get_obj(key)
        prev_obj.next = value
        value.next = next_obj
        obj.next = None


if __name__ == '__main__':
    st = Stack()
    st.push(StackObj("obj1"))
    st.push(StackObj("obj2"))
    st.push(StackObj("obj3"))
    st[1] = StackObj("new obj2")
    print(st[2].data)  # obj3
    print(st[1].data)  # new obj2
    print(st.pop())
    print(st.pop())
    print(st.pop())
    print(st.pop())
    # res = st[3]  # исключение IndexError
