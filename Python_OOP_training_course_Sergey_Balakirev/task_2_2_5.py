class WindowDlg:
    def __init__(self, title, width, height):
        self.__title = title
        self.__width = width
        self.__height = height

    def show(self):
        print(f'{self.__title}: {self.__width}, {self.__height}')

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int) and 0 <= value <= 10000:
            self.__width = value
            self.show()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int) and 0 <= value <= 10000:
            self.__height = value
            self.show()


if __name__ == '__main__':
    win = WindowDlg('Dialog', 100, 100)
    win.width = 200
    win.height = 300
    print(win.width)
    print(win.height)
