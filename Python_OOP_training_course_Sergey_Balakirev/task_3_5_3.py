class Track:
    def __init__(self, start_x: (int, float), start_y: (int, float)):
        self.start_x = start_x
        self.start_y = start_y
        self.__tracks = []

    def add_track(self, tr: object):
        self.__tracks.append(tr)

    def get_tracks(self):
        return tuple(self.__tracks)

    def __len__(self):
        len_track = 0
        start_x = self.start_x
        start_y = self.start_y
        for track in self.__tracks:
            len_track += ((track.to_x - start_x)**2 + (track.to_y - start_y)**2) ** 0.5
            start_x = track.to_x
            start_y = track.to_y
        return int(len_track)

    def __eq__(self, other: object):
        if not isinstance(other, Track):
            raise TypeError('Объекты сравнения должны иметь тип Track')
        return len(self) == len(other)

    def __lt__(self, other):
        if not isinstance(other, Track):
            raise TypeError('Объекты сравнения должны иметь тип Track')
        return len(self) < len(other)


class TrackLine:
    def __init__(self, to_x: (int, float), to_y: (int, float), max_speed: int):
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed


if __name__ == '__main__':
    track1, track2 = Track(0, 0), Track(0, 1)
    track1.add_track(TrackLine(2, 4, 100))
    track1.add_track(TrackLine(5, -4, 100))
    track2.add_track(TrackLine(3, 2, 90))
    track2.add_track(TrackLine(10, 8, 90))
    res_eq = track1 == track2
    print(res_eq)