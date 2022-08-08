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


####


class TicTacToe:
    def __init__(self):
        self.pole = [[Cell() for _ in range(3)]for _ in range(3)]

    def clear(self):
        self.pole = [[Cell() for _ in range(3)]for _ in range(3)]

    def __getitem__(self, item):
        if type(item[1]) == int and type(item[0]) == int:
            return self.pole[item[0]][item[1]].value

        if type(item[1]) == slice:
            res = self.pole[item[0]][item[1]]
            return tuple(i.value for i in res)

        if type(item[0]) == slice:
            pole = [[0 for _ in range(3)] for _ in range(3)]
            for i in range(3):
                for j in range(3):
                    pole[i][j] = self.pole[j][i]
            return tuple(i.value for i in pole[item[1]])

    def __setitem__(self, key, value):
        if -1 >= key[0] >= 3 or -1 >= key[1] >= 3:
            raise IndexError('неверный индекс клетки')

        if bool(self.pole[key[0]][key[1]]):
            self.pole[key[0]][key[1]].value = value
            self.pole[key[0]][key[1]].is_free = False
        else:
            raise ValueError('клетка уже занята')
        return self


class Cell:
    def __init__(self):
        self.is_free = True
        self.value = 0

    def __bool__(self):
        return self.is_free


g = TicTacToe()
g.clear()
assert g[0, 0] == 0 and g[2, 2] == 0, "начальные значения всех клеток должны быть равны 0"
g[1, 1] = 1
g[2, 1] = 2
assert g[1, 1] == 1 and g[
    2, 1] == 2, "неверно отработала операция присваивания новых значений клеткам игрового поля (или, некорректно работает считывание значений)"

try:
    res = g[3, 0]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError при считывании из несуществующей ячейки"

try:
    g[3, 0] = 5
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError при записи в несуществующую ячейку"

g.clear()
g[0, 0] = 1
g[1, 0] = 2
g[2, 0] = 3

assert g[0, :] == (1, 0, 0) and g[1, :] == (2, 0, 0) and g[:, 0] == (
1, 2, 3), "некорректно отработали срезы после вызова метода clear() и присваивания новых значений"

cell = Cell()
assert cell.value == 0, "начальное значение атрибута value класса Cell должно быть равно 0"
res = cell.is_free
cell.is_free = True
assert bool(cell), "функция bool вернула False для свободной клетки"

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



############


class IntegerValue:
    @classmethod
    def verify_val(cls, coord):
        if type(coord) != int:
            raise ValueError('возможны только целочисленные значения')

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_val(value)
        setattr(instance, self.name, value)


class StringValue:
    @classmethod
    def verify_val(cls, coord):
        if type(coord) != str:
            raise ValueError('возможны только string значения')

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_val(value)
        setattr(instance, self.name, value)


class TableValues:
    def __init__(self, rows, cols, cell):
        if cell:
            self.cells = tuple(tuple(cell() for _ in range(cols))for _ in range(rows))
        else:
            raise ValueError('параметр cell не указан')

    def __getitem__(self, item):
        if 0 <= item[0] < len(self.cells) and 0 <= item[1] < len(self.cells):
            return self.cells[item[0]][item[1]].value
        else:
            raise IndexError('неверный индекс для доступа к элементам массива')

    def __setitem__(self, key, value):
        if 0 <= key[0] < len(self.cells) and 0 <= key[1] < len(self.cells):
            self.cells[key[0]][key[1]].value = value
        else:
            raise IndexError('неверный индекс для доступа к элементам массива')


class CellInteger:
    value = IntegerValue()

    def __init__(self, start_value=0):
        self.value = start_value


class CellString:
    value = StringValue()

    def __init__(self, start_value='_'):
        self.value = start_value

table = TableValues(2, 3, cell=CellInteger)
print(table[0, 1])
table[1, 1] = 10
# table[0, 0] = 1.45 # генерируется исключение ValueError

# вывод таблицы в консоль
for row in table.cells:
    for x in row:
        print(x.value, end=' ')
    print()


tb1 = TableValues(3, 2, cell=CellString)
tb1[0, 0] = '1'
tb1[1, 1] = '2'

for row in tb1.cells:
    for x in row:
        print(x.value, end=' ')
    print()


tb = TableValues(3, 2, cell=CellInteger)
tb[0, 0] = 1
assert tb[0, 0] == 1, "некорректно работает запись и/или считывание значения в ячейку таблицы по индексам"

try:
    tb[2, 1] = 1.5
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

for row in tb.cells:
    for x in row:
        assert isinstance(x, CellInteger), "коллекция cells должна содержать только объекты класса  CellInteger"

cell = CellInteger(10)
assert cell.value == 10, "дескриптор value вернул неверное значение"


#####


class RadiusVector:
    """
    P.S. При передаче среза в магических методах __setitem__() и __getitem__() параметр индекса становится объектом 
    класса slice. Его можно указывать непосредственно в квадратных скобках упорядоченных коллекций 
    (списков, кортежей и т.п.).
    """
    def __init__(self, *args):
        self.coords = [*args]

    def __getitem__(self, item):
        res = self.coords[item]
        return res if isinstance(res, (int, float)) else tuple(res)

    def __setitem__(self, key, value):
        self.coords[key] = value
        return self


v = RadiusVector(1, 1, 1, 1)
print(v[1]) # 1
print(v[1:3]) # 1
v[:] = 1, 2, 3, 4
print(v[2]) # 3
print(v[1:]) # (2, 3, 4)
v[0] = 10.5



#############


class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.bag = []

    def add_thing(self, thing):
        if self.get_bag_weight() + thing.weight > self.max_weight:
            raise ValueError('превышен суммарный вес предметов')
        self.bag.append(thing)

    def get_bag_weight(self):
        w = 0
        for i in self.bag:
            w += i.weight
        return w

    def check_index(self, index):
        if 0 > index >= len(self.bag):
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.check_index(item)
        return self.bag[item]

    def __setitem__(self, key, value):
        self.check_index(key)
        if self.get_bag_weight() - self.bag[key].weight + value.weight <= self.max_weight:
            self.bag[key] = value
        else:
            raise ValueError('превышен суммарный вес предметов')

    def __delitem__(self, key):
        self.check_index(key)
        del self.bag[key]
        return self

class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


b = Bag(700)
b.add_thing(Thing('книга', 100))
b.add_thing(Thing('носки', 200))

try:
    b.add_thing(Thing('рубашка', 500))
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

assert b[0].name == 'книга' and b[
    0].weight == 100, "атрибуты name и weight объекта класса Thing принимают неверные значения"

t = Thing('Python', 20)
b[1] = t
assert b[1].name == 'Python' and b[
    1].weight == 20, "неверные значения атрибутов name и weight, возможно, некорректно работает оператор присваивания с объектами класса Thing"

del b[0]
assert b[0].name == 'Python' and b[0].weight == 20, "некорректно отработал оператор del"

try:
    t = b[2]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

b = Bag(700)
b.add_thing(Thing('книга', 100))
b.add_thing(Thing('носки', 200))

b[0] = Thing('рубашка', 500)

try:
    b[0] = Thing('рубашка', 800)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при замене предмета в объекте класса Bag по индексу"

    
