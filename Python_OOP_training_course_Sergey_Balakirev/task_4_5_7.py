from abc import ABC, abstractmethod


class StackInterface(ABC):

    @abstractmethod
    def push_back(self, obj):
        pass

    @abstractmethod
    def pop_back(self):
        pass


class Stack(StackInterface):
    def __init__(self):
        self._top = None
        self._end = None

    def push_back(self, obj: object):
        if self._top is None:
            self._top = obj
            self._end = obj
        else:
            self._end._next = obj
            self._end = obj

    def pop_back(self):
        if self._top == self._end:
            del_obj = self._top
            self._top = self._end = None
        else:
            obj = self._top
            while obj._next != self._end:
                obj = obj._next
            del_obj = self._end
            self._end = obj
            self._end._next = None
        return del_obj


class StackObj:
    def __init__(self, data: str):
        self._data = data
        self._next = None


if __name__ == '__main__':
    st = Stack()
    st.push_back(StackObj("obj 1"))
    obj = StackObj("obj 2")
    st.push_back(obj)
    del_obj = st.pop_back()  # del_obj - ссылка на удаленный объект (если объектов не было, то del_obj = None)
    print(del_obj)
    del_obj = st.pop_back()
    print(del_obj)
    del_obj = st.pop_back()
    print(del_obj)
