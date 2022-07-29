class Clock:
    """
    Магические методы __add__, __sub__, __mul__, __truediv__
    https://stepik.org/lesson/701989/step/1?unit=702090
    """
    __DAY = 86400  # number of seconds in one day

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError('Seconds should be integer')
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f'{self.__get_formated(h)}:{self.__get_formated(m)}:{self.__get_formated(s)}'

    @classmethod
    def __get_formated(cls, x):
        return str(x).rjust(2, '0')

    def __add__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('Should be integer or Clock obj on right')
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
        return Clock(self.seconds + sc)

    def __radd__(self, other):   # for c1 = 100 + c1
        return self + other

    def __iadd__(self, other):   # for c1 += 100
        print('__iadd__')
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('Should be integer or Clock obj on right')

        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
        self.seconds += sc
        return self


c1 = Clock(1000)
c2 = Clock(2000)
c3 = Clock(3000)
c1.seconds = c1.seconds + 100
c1 = c1+100
print(c1.get_time())
c1 = 100 + c1
print(c1.get_time())
c1 += 100
print(c1.get_time())
c4 = c1+c2+c3
print(c4.get_time())
