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
        if isinstance(obj, (StackObj, None)):
            self.__next = obj


class Stack:
    def __init__(self, top=None):
        self.top = top

    def push(self, obj: object):
        if self.top is None:
            self.top = obj
        else:
            self.top.next =

