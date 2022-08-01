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



######


class ListMath:
    def __init__(self, lst=None):
        self.lst_math = [x for x in lst if type(x) in (int, float)] if lst and type(lst) == list else []

    def get_list(self):
        return self.lst_math

    @staticmethod
    def checker(other):
        if not isinstance(other, (int, float)):
            raise ArithmeticError('Should be int or float')
        return True

    def __add__(self, other):
        self.checker(other)
        return ListMath([i + other for i in self.get_list()[:]])

    def __radd__(self, other):
        self.checker(other)
        return ListMath([other + i for i in self.get_list()[:]])

    def __iadd__(self, other):
        self.checker(other)
        self.lst_math = [i + other for i in self.get_list()[:]]
        return self

    def __sub__(self, other):
        self.checker(other)
        return ListMath([i - other for i in self.get_list()[:]])

    def __rsub__(self, other):
        self.checker(other)
        return ListMath([other - i for i in self.get_list()[:]])

    def __isub__(self, other):
        self.checker(other)
        self.lst_math = [i - other for i in self.get_list()[:]]
        return self

    def __mul__(self, other):
        self.checker(other)
        return ListMath([i * other for i in self.get_list()[:]])

    def __rmul__(self, other):
        self.checker(other)
        return ListMath([other * i for i in self.get_list()[:]])

    def __imul__(self, other):
        self.checker(other)
        self.lst_math = [i * other for i in self.get_list()[:]]
        return self

    def __truediv__(self, other):
        self.checker(other)
        if other == 0:
            raise 'Should be > 0'
        return ListMath([i / other for i in self.get_list()[:]])

    def __rtruediv__(self, other):
        self.checker(other)
        if other == 0:
            raise 'Should be > 0'
        return ListMath([other / i for i in self.get_list()[:]])

    def __itruediv__(self, other):
        self.checker(other)
        if other == 0:
            raise 'Should be > 0'
        self.lst_math = [i / other for i in self.get_list()[:]]
        return self


lst1 = ListMath()
lp = [1, False, 2, -5, "abc", 7]
lst2 = ListMath(lp)
lst3 = ListMath(lp)

assert id(lst2.lst_math) != id(lst3.lst_math), "внутри объектов класса ListMath должна создаваться копия списка"

assert lst1.lst_math == [] and lst2.lst_math == [1, 2, -5, 7], "неверные значения в списке объекта класса ListMath"

res1 = lst2 + 76
lst = ListMath([1, 2, 3])
lst += 5
assert lst.lst_math == [6, 7, 8] and res1.lst_math == [77, 78, 71, 83], "неверные значения, полученные при операциях сложения"

lst = ListMath([0, 1, 2])
res3 = lst - 76
res4 = 7 - lst
assert res3.lst_math == [-76, -75, -74] and res4.lst_math == [7, 6, 5], "неверные значения, полученные при операциях вычитания"

lst -= 3
assert lst.lst_math == [-3, -2, -1], "неверные значения, полученные при операции вычитания -="

lst = ListMath([1, 2, 3])
res5 = lst * 5
res6 = 3 * lst
lst *= 4
assert res5.lst_math == [5, 10, 15] and res6.lst_math == [3, 6, 9], "неверные значения, полученные при операциях умножения"
assert lst.lst_math == [4, 8, 12], "неверные значения, полученные при операциях умножения"

lst = lst / 2
lst /= 13.0


####

class Stack:
    def __init__(self):
        self.top = None

    def push_back(self, obj):
        if self.top is None:
            self.top = obj
        else:
            cur = self.top
            while cur.next:
                cur = cur.next
            cur.next = obj

    def pop_back(self):
        if self.top:
            cur = self.top
            obj = None
            while cur.next:
                obj = cur
                cur = cur.next
            obj.next = None
        else:
            self.top = None

    def __add__(self, other):
        if not isinstance(other, StackObj):
            raise TypeError('Should be StackObj type')
        self.push_back(other)
        return self

    def __mul__(self, other):
        for i in other:
            self.push_back(StackObj(i))
        return self


class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        self.__next = next


assert hasattr(Stack, 'pop_back'), "класс Stack должен иметь метод pop_back"

st = Stack()
top = StackObj("1")
st.push_back(top)
assert st.top == top, "неверное значение атрибута top"

st = st + StackObj("2")
st = st + StackObj("3")
obj = StackObj("4")
st += obj

st = st * ['data_1', 'data_2']
st *= ['data_3', 'data_4']

d = ["1", "2", "3", "4", 'data_1', 'data_2', 'data_3', 'data_4']
h = top
i = 0
while h:
    assert h._StackObj__data == d[
        i], "неверное значение атрибута __data, возможно, некорректно работают операторы + и *"
    h = h._StackObj__next
    i += 1

assert i == len(d), "неверное число объектов в стеке"
