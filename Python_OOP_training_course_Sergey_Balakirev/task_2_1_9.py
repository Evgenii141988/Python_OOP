class ObjList:
    def __init__(self, data):
        self.__data = data
        self.__next = None
        self.__prev = None

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        if self.head is None and self.tail is None:
            self.head = obj
            self.tail = obj
        else:
            self.tail.set_next(obj)
            obj.set_prev(self.tail)
            self.tail = obj

    def remove_obj(self):
        self.tail = self.tail.get_prev()
        self.tail.set_next(None)

    def get_data(self):
        datas = []
        obj = self.head
        while obj is not None:
            datas.append(obj.get_data())
            obj = obj.get_next()
        return datas


if __name__ == '__main__':
    lst = LinkedList()
    lst.add_obj(ObjList("данные 1"))
    lst.add_obj(ObjList("данные 2"))
    lst.add_obj(ObjList("данные 3"))
    lst.remove_obj()
    print(lst.tail.get_data())
    res = lst.get_data()
    print(res)
