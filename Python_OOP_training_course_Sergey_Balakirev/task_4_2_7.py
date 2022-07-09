class VideoItem:
    def __init__(self, title: str, descr: str, path):
        self.title = title
        self.descr = descr
        self.path = path
        self.rating = VideoRating()


class VideoRating:
    def __init__(self):
        self.__rating = 0

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value: int):
        if not 0 <= value <= 5:
            raise ValueError('неверное присваиваемое значение')
        self.__rating = value


if __name__ == '__main__':
    v = VideoItem('Курс по Python ООП', 'Подробный курс по Python ООР', 'D:/videos/python_oop.mp4')
    print(v.rating.rating)  # 0
    v.rating.rating = 5
    print(v.rating.rating)  # 5
    title = v.title
    descr = v.descr
    v.rating.rating = 6  # ValueError
