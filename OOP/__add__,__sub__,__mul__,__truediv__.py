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



###

"""
https://stepik.org/lesson/701989/step/5?unit=702090
https://www.youtube.com/watch?v=tkjqkiCSnqM
"""
class NewList:
    def __init__(self, lst=None):
        self.lst = lst[:] if lst and type(lst) == list else []

    def get_list(self):
        return self.lst

    def __sub__(self, other):
        if not isinstance(other, (list, NewList)):
            raise ArithmeticError('Should be list or NewList obj on right')

        ls = other
        if isinstance(other, NewList):
            ls = other.get_list()

        return NewList(self.__diff_list(self.lst, ls))

    @staticmethod
    def __diff_list(ls1, ls2):
        if len(ls2) == 0:
            return ls1

        sub = ls2[:]
        return [x for x in ls1 if not NewList.__is_element(x, sub)]

    @staticmethod
    def __is_element(x, sub):
        res = any(map(lambda xx: type(x) == type(xx) and x == xx, sub))
        if res:
            sub.remove(x)
        return res

    def __rsub__(self, other):
        if not isinstance(other, (list, NewList)):
            raise ArithmeticError('Should be list or NewList obj on right')
        return NewList(self.__diff_list(other, self.lst))


lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])
res_1 = lst1 - lst2   # NewList: [-4, 6, 10, 11, 15, False]
print(res_1.get_list())
lst1 -= lst2   # NewList: [-4, 6, 10, 11, 15, False]
print(lst1.get_list())
print('lst2', lst2.get_list())
res_2 = lst2 - [0, True]
print(res_2.get_list())
res_2 = lst2 - [0, True]   # NewList: [1, 2, 3]
print(res_2.lst)
res_3 = [1, 2, 3, 4.5] - res_2   # NewList: [4.5]
print(res_3.lst)
a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]
print(res_4.get_list())
