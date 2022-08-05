"""
Магические методы __getitem__, __setitem__ и __delitem__
https://stepik.org/lesson/701993/step/1?unit=702094
"""
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):  # For obj[item]
        if 0<= item < len(self.marks):
            return self.marks[item]
        else:
            raise IndexError('Wrong index')

    def __setitem__(self, key, value):   # For obj[key] = value
        if not isinstance(key, int) or key < 0:
            raise TypeError('Wrong key')

        if key >= len(self.marks):
            off = key + 1 - len(self.marks)
            self.marks.extend([None] * off)
        self.marks[key] = value

    def __delitem__(self, key):   # For del odj[key]
        if not isinstance(key, int) or key < 0:
            raise TypeError('Wrong key')

        del self.marks[key]



s1 = Student('Vitalii', [5, 5, 3, 2, 5])
s1[2] = 4
print(s1[2])
del s1[2]
s1[10] = 5
print(s1.marks)

##########


class Record:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            self.__dict__[k] = v

    def __getitem__(self, item):
        keys = [*self.__dict__.keys()]

        if 0 <= item < len(self.__dict__):
            key = keys[item]
            return self.__dict__[key]
        else:
            raise IndexError('неверный индекс поля')

    def __setitem__(self, key, value):
        keys = [*self.__dict__.keys()]

        if 0 <= key < len(self.__dict__):
            k = keys[key]
            self.__dict__[k] = value
        else:
            raise IndexError('неверный индекс поля')
            
            
#####


class Track:
    def __init__(self, start_x, start_y):
        self.x = start_x
        self.y = start_y
        self.road = [[(self.x, self.y), None]]

    def add_point(self, x, y, speed):
        self.road.append([(x, y), speed])

    def __getitem__(self, item):
        if 0 <= item < len(self.road)-1:
            return self.road[item+1][0], self.road[item+1][1]
        else:
            raise IndexError('некорректный индекс')

    def __setitem__(self, key, value):
        if 0 <= key < len(self.road) - 1:
            if type(value) in (float, int):
                self.road[key+1][1] = value
        else:
            raise IndexError('некорректный индекс')


tr = Track(10, -5.4)
tr.add_point(20, 0, 100)  # первый линейный сегмент: indx = 0
tr.add_point(50, -20, 80)  # второй линейный сегмент: indx = 1
tr.add_point(63.45, 1.24, 60.34)  # третий линейный сегмент: indx = 2

tr[2] = 60
c, s = tr[2]
print(c, s)  # => (63.45, 1.24) 60
res = tr[3]  # IndexError


#########


class Array:
    def __init__(self, max_length, cell):
        self.cell = cell
        self.l = [self.cell() for _ in range(max_length)]

    def __getitem__(self, item):
        if 0 <= item < len(self.l):
            return self.l[item].val
        else:
            raise IndexError('неверный индекс для доступа к элементам массива')

    def __setitem__(self, key, value):
        if 0 <= key < len(self.l):
            self.l[key].val = value
        else:
            raise IndexError('неверный индекс для доступа к элементам массива')

    def __repr__(self):
        s = [str(i.val) for i in self.l]
        return ' '.join(s)


class Integer:
    def __init__(self, start_value=0):
        self.val = start_value

    @property
    def val(self):
        return self.__value

    @val.setter
    def val(self, val):
        if type(val) == int:
            self.__value = val
        else:
            raise ValueError('должно быть целое число')

ar_int = Array(20, cell=Integer)
assert ar_int[18] == 0, "начальные значения в ячейках массива (в объектах класса Integer) должны быть равны 0"
print(ar_int[3])
print(ar_int) # должны отображаться все значения массива в одну строчку через пробел
ar_int[1] = 10
print(ar_int)
# ar_int[1] = 10.5 # должно генерироваться исключение ValueError
# ar_int[10] = 1 # должно генерироваться исключение IndexError
