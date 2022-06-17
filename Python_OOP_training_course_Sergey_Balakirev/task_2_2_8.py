class TreeObj:
    def __init__(self, indx: int, value: str = None):
        self.indx = indx
        self.value = value
        self.left = None
        self.right = None

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, obj: object):
        self.__left = obj

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, obj: object):
        self.__right = obj


class DecisionTree:
    @classmethod
    def predict(cls, root: object, x: list):
        while root.left and root.right:
            if x[root.indx] == 1:
                root = root.left
            else:
                root = root.right
        return root.value

    @classmethod
    def add_obj(cls, obj: object, node: object = None, left: bool = True) -> object:
        if node:
            if left:
                node.left = obj
            else:
                node.right = obj
        return obj


if __name__ == '__main__':
    root = DecisionTree.add_obj(TreeObj(0))
    v_11 = DecisionTree.add_obj(TreeObj(1), root)
    v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
    DecisionTree.add_obj(TreeObj(-1, "будет программистом"), v_11)
    DecisionTree.add_obj(TreeObj(-1, "будет кодером"), v_11, False)
    DecisionTree.add_obj(TreeObj(-1, "не все потеряно"), v_12)
    DecisionTree.add_obj(TreeObj(-1, "безнадежен"), v_12, False)

    x = [0, 0, 0]
    res = DecisionTree.predict(root, x)  # будет программистом
    print(res)
