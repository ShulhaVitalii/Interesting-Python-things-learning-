class Cat:
  """
  https://stepik.org/lesson/701988/step/1?unit=702089
  Магические методы __str__, __repr__, __len__, __abs__
  """
    def __init__(self, name):
        self.name = name

    # using for debug
    def __repr__(self):
        return f'{self.__class__}: {self.name}'

    def __str__(self):
        return f'{self.name}'


cat = Cat('Kitty')

print(cat)


class Point:
    def __init__(self, *args):
        self.__coords = args

    def __len__(self):
        return len(self.__coords)

    def __abs__(self):
        return list(map(abs, self.__coords))


p = Point(1, -2, -5)
print(len(p)) # => 3
print(abs(p)) # => [1, 2, 5]

####


class Model:
    def __init__(self):
        self.data = {}

    def query(self, **kwargs):
        for i, v in kwargs.items():
            self.data[i] = v

    def __str__(self):
        if self.data is None:
            return "Model"
        s = "Model: "
        for i in self.data:
            s += f'{i} = {self.data[i]}, '
        return s[:-2]


model = Model()
print(model)
model.query(id=1, fio='Sergey', old=33)
print(model)



###


class WordString:
    def __init__(self, string=''):
        self.__string = string

    def __len__(self):
        return len(self.__string.split())

    def __call__(self, *args, **kwargs):
        return self.__string.split()[args[0]]

    @property
    def string(self):
        return self.__string
    @string.setter
    def string(self, string):
        self.__string = string

words = WordString("1 2      3   4 5 6 7")
print(len(words))
print(words(2))
words = WordString()
words.string = "Курс по Python ООП"
n = len(words)
first = "" if n == 0 else words(0)
print(words.string)
print(f"Число слов: {n}; первое слово: {first}")



############

class LinkedList:
    """
    https://stepik.org/lesson/701988/step/6?unit=702089
    https://www.youtube.com/watch?v=6-xKuQp9b7Y
    Объявите класс LinkedList (связный список) для работы со следующей структурой данных:
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        obj.prev = self.tail
        if self.tail:
            self.tail.next = obj
        self.tail = obj

        if not self.head:
            self.head = obj

    def __get_obj_by_index(self, indx):
        h = self.head
        n = 0
        while h and n < indx:
            h = h.next
            n += 1
        return h

    def remove_obj(self, indx):
        obj = self.__get_obj_by_index(indx)
        if obj is None:
            return

        p, n = obj.prev, obj.next
        if p:
            p.next = n
        if n:
            n.prev = p

        if self.head == obj:
            self.head = n
        if self.tail == obj:
            self.tail = p

    def __len__(self):
        n = 0
        h = self.head
        while h:
            n += 1
            h = h.next
        return n

    def __call__(self,indx, *args, **kwargs):
        obj = self.__get_obj_by_index(indx)
        return obj.data if obj else None

class ObjList:
    def __init__(self, data):
        self.__data = ''
        self.data = data
        self.__prev = None
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        if type(data) is str:
            self.__data = data

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, obj):
        if type(obj) in (ObjList, type(None)):
            self.__prev = obj

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        if type(obj) in (ObjList, type(None)):
            self.__next = obj

linked_lst = LinkedList()
linked_lst.add_obj(ObjList("Sergey"))
linked_lst.add_obj(ObjList("Balakirev"))
linked_lst.add_obj(ObjList("Python"))
linked_lst.remove_obj(2)
linked_lst.add_obj(ObjList("Python ООП"))
n = len(linked_lst)  # n = 3
s = linked_lst(1) # s = Balakirev


#######

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    @property
    def real(self):
        return self.__real

    @real.setter
    def real(self, real):
        if type(real) not in [int, float]:
            raise ValueError("Неверный тип данных.")
        else:
            self.__real = real

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, img):
        if type(img) not in [int, float]:
            raise ValueError("Неверный тип данных.")
        else:
            self.__img = img

    def __abs__(self):
        return (self.real**2 + self.img**2) ** 0.5


cmp = Complex(7, 8)
cmp.real = 3
cmp.img = 4
c_abs = abs(cmp)



###


class DeltaClock:
    def __init__(self, clock1, clock2):
        self.clock1 = clock1
        self.clock2 = clock2

    def __str__(self):
        h = self.clock1.hours - self.clock2.hours if self.clock1.hours > self.clock2.hours else 0
        m = self.clock1.minutes - self.clock2.minutes if self.clock1.minutes > self.clock2.minutes else 0
        s = self.clock1.seconds - self.clock2.seconds if self.clock1.seconds > self.clock2.seconds else 0

        return f'{h:02}: {m:02}: {s:02}'

    def __len__(self):
        return self.clock1.get_time() - self.clock2.get_time() if self.clock1.get_time() - self.clock2.get_time() >0 else 0


class Clock:
    def __init__(self, hours, minutes, seconds):
        if self.checker(hours):
            self.hours = hours
        if self.checker(minutes):
            self.minutes = minutes
        if self.checker(seconds):
            self.seconds = seconds

    @staticmethod
    def checker(time):
        if type(time) is int and time >= 0:
            return True
        return False

    def get_time(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

dt = DeltaClock(Clock(1, 15, 15), Clock(3, 45, 15))

str_dt = str(dt)
print(str_dt)
print(dt) # 01: 30: 00
len_dt = len(dt) # 5400
print(len_dt)
