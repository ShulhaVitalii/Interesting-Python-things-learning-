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
