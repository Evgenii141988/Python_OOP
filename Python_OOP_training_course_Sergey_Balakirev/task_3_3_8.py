class DeltaClock:
    def __init__(self, clock1: object, clock2: object):
        self.clock1 = clock1
        self.clock2 = clock2

    def __str__(self):
        d_time = self.clock1.get_time() - self.clock2.get_time()
        if d_time <= 0:
            return '00: 00: 00'
        hours = d_time // 3600
        minutes = d_time % 3600 // 60
        seconds = d_time % 3600 % 60
        return f'{hours:0>2}: {minutes:0>2}: {seconds:0>2}'

    def __len__(self):
        if self.clock1.get_time() - self.clock2.get_time() >= 0:
            return self.clock1.get_time() - self.clock2.get_time()
        return 0


class Clock:
    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds


if __name__ == '__main__':
    dt = DeltaClock(Clock(5, 0, 0), Clock(1, 59, 59))
    print(dt)  # 01: 30: 00
    len_dt = len(dt)  # 5400
    print(len_dt)
