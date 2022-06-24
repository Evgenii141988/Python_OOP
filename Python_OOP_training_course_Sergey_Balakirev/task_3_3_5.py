class ObjList:
    def __init__(self, data: str):
        self.__data = data
        self.__prev = None
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, value):
        self.__prev = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.obj_lst = []

    def add_obj(self, obj: object):
        if self.tail is None:
            self.head = obj
            self.tail = obj
            self.obj_lst.append(obj)
        else:
            self.tail.next = obj
            obj.prev = self.tail
            self.tail = obj
            self.obj_lst.append(obj)

    def remove_obj(self, indx: int):
        if len(self.obj_lst) != 1:
            if indx == 0:
                self.obj_lst[1].prev = None
                self.head = self.obj_lst[1]
                self.obj_lst.pop(indx)
            elif indx == len(self.obj_lst) - 1:
                self.obj_lst[indx - 1].next = None
                self.tail = self.obj_lst[indx - 1]
            else:
                self.obj_lst[indx - 1].next = self.obj_lst[indx + 1]
                self.obj_lst[indx + 1].prev = self.obj_lst[indx - 1]
        else:
            self.head = None
            self.tail = None
        self.obj_lst[indx].prev = self.obj_lst[indx].next = None
        self.obj_lst.pop(indx)

    def __len__(self):
        return len(self.obj_lst)

    def __call__(self, indx: int, *args, **kwargs):
        return self.obj_lst[indx].data


if __name__ == '__main__':
    linked_lst = LinkedList()
    linked_lst.add_obj(ObjList("Sergey"))
    linked_lst.add_obj(ObjList("Balakirev"))
    linked_lst.add_obj(ObjList("Python"))
    linked_lst.remove_obj(2)
    linked_lst.add_obj(ObjList("Python ООП"))
    n = len(linked_lst)  # n = 3
    s = linked_lst(1)  # s = Balakirev
    print(n)
    print(s)
    print(linked_lst(0))
    print(linked_lst(1))
    print(linked_lst(2))
