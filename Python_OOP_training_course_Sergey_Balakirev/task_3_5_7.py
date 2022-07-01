class FileAcceptor:
    def __init__(self, *args):
        self.__exts = list(args)

    def __call__(self, filename: str):
        return any((f'.{ext}' in filename for ext in self.__exts))

    def __add__(self, other: object):
        if not isinstance(other, FileAcceptor):
            raise TypeError('Объекты сложения должны иметь тип FileAcceptor')
        return FileAcceptor(*list(set(self.__exts + other.__exts)))


if __name__ == '__main__':
    filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.xls"]
    acceptor_images = FileAcceptor("jpg", "jpeg", "png")
    acceptor_docs = FileAcceptor("txt", "doc", "xls")
    filenames = list(filter(acceptor_images + acceptor_docs, filenames))
