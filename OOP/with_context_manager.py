"""
Менеджеры контекстов. Оператор with
    __enter__
    __exit__
"""

class DefenderVector:
    def __init__(self, v):
        self.__v = v

    def __enter__(self):
        self.__temp = self.__v[:]
        return self.__temp

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.__v[:] = self.__temp

        return False


v1 = [1, 2, 3]
v2 = [2, 3]
try:
    with DefenderVector(v1) as dv:
        for i, a in enumerate(dv):
            dv[i] += v2[i]
except:
    print("Error")
print(v1)


#####


class ConnectionError(Exception):
    pass

class DatabaseConnection:
    def __init__(self):
        self._fl_connection_open = False

    def connect(self, login, password):
        self._fl_connection_open = True
        raise ConnectionError

    def close(self):
        self._fl_connection_open = False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        return False


with DatabaseConnection() as conn:
    try:
        conn.connect('www', 12345)
    except ConnectionError as e:
        pass


c = DatabaseConnection()

try:
    c.connect('aaa', 'bbb')
except ConnectionError:
    assert c._fl_connection_open
else:
    assert False, "не сгенерировалось исключение ConnectionError"

try:
    with DatabaseConnection() as conn:
        conn.connect('aaa', 'bbb')
except ConnectionError:
    assert True
else:
    assert False, "не сгенерировалось исключение ConnectionError"

assert conn._fl_connection_open == False, "атрибут _fl_connection_open принимает значение True, а должно быть False"


######

from copy import deepcopy


class Box:
    def __init__(self, name, max_weight, things=[]):
        self._name = name
        self._max_weight = max_weight
        self._things = things

    def _get_box_weight(self):
        w = 0
        for i in self._things:
            w += i[-1]
        return w

    def add_thing(self, obj):
        if self._get_box_weight() + obj[1] <= self._max_weight:
            self._things.append(obj)
        else:
            raise ValueError('превышен суммарный вес вещей')


class BoxDefender:
    def __init__(self, c):
        self.__c = c

    def __enter__(self):
        self.__temp = deepcopy(self.__c)
        return self.__temp

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            for i in self.__temp._things:
                if i not in self.__c._things:
                    self.__c.add_thing(i)
        return False


b = Box('name', 2000)
assert b._name == 'name' and b._max_weight == 2000, "неверные значения атрибутов объекта класса Box"

b.add_thing(("1", 100))
b.add_thing(("2", 200))

try:
    with BoxDefender(b) as bb:
        bb.add_thing(("3", 1000))
        bb.add_thing(("4", 1900))
except ValueError:
    print(b._things)
    assert len(b._things) == 2, f'{len(b._things)}'

else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    with BoxDefender(b) as bb:
        bb.add_thing(("3", 100))
except ValueError:
    assert False, "возникло исключение ValueError, хотя, его не должно было быть"
else:
    assert len(b._things) == 3, "неверное число элементов в списке _things"

