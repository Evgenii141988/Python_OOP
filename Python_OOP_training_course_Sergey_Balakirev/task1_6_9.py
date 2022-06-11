class Video:
    def create(self, name):
        self.name = name

    def play(self):
        print(f'воспроизведение видео {self.name}')


class YouTube:
    VIDEOS = []

    @classmethod
    def add_video(cls, video):
        cls.VIDEOS.append(video)

    @classmethod
    def play(cls, video_indx):
        return cls.VIDEOS[video_indx].play()


if __name__ == '__main__':
    v1 = Video()
    v2 = Video()
    v1.create('Python')
    v2.create('Python ООП')
    YouTube.add_video(v1)
    YouTube.add_video(v2)
    YouTube.play(0)
    YouTube.play(1)
