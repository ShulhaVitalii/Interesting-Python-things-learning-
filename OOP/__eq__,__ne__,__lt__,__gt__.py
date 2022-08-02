"""
Методы сравнений __eq__, __ne__, __lt__, __gt__ и другие
https://stepik.org/lesson/701990/step/1?unit=702091
"""

class Clock:

    __DAY = 86400  # number of seconds in one day

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError('Seconds should be integer')
        self.seconds = seconds % self.__DAY

    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError('Int Clock')

        return other if isinstance(other, int) else other.seconds

    def __eq__(self, other):   # == work for != like not(x == y)
        sc = self.__verify_data(other)
        return self.seconds == sc

    def __lt__(self, other):   # x < y  work for > like y > x
        sc = self.__verify_data(other)
        return self.seconds < sc

    def __gt__(self, other):
        sc = self.__verify_data(other)
        return self.seconds > sc

    def __le__(self, other):   # x <= y  work for >= like y >= x
        sc = self.__verify_data(other)
        return self.seconds <= sc

    def __ge__(self, other):
        sc = self.__verify_data(other)
        return self.seconds >= sc

c1 = Clock(1000)
c2 = Clock(2000)
print(c1 == c2)
print(c1 != c2)
print(c1 > c2)
print(c1 < c2)
print(c1 >= c2)
print(c1 <= c2)



#########


class Track:
    def __init__(self, start_x=0, start_y=0):
        # self.start_x = start_x
        # self.start_y = start_y
        self.track = [TrackLine(start_x, start_y)]

    def add_track(self, tr):
        self.track.append(tr)

    def get_tracks(self):
        return tuple(self.track)

    def __len__(self):
        l = 0
        for i in range(len(self.track)-1):
            l += ((self.track[i].to_x - self.track[i+1].to_x)**2 + (self.track[i].to_y - self.track[i+1].to_y)**2)**0.5

        return int(l)

    def __eq__(self, other):
        return len(self) == len(other)

    def __lt__(self, other):
        return len(self) < len(other)


class TrackLine:
    def __init__(self, to_x, to_y, max_speed=0):
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed


track1, track2 = Track(), Track(0, 1)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))
res_eq = track1 == track2
print(res_eq)
print(len(track1))
print(len(track2))

