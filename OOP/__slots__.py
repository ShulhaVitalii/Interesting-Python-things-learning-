"""
Коллекция __slots__
"""
import timeit


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calk(self):
        self.x += 1
        del self.y
        self.y = 0


class Point2D:
    __slots__ = ('x', 'y')   # To allow local attributes.  After that __dict__ does not exist

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calk(self):
        self.x += 1
        del self.y
        self.y = 0


pt = Point(10, 20)
print(pt.__sizeof__() + pt.__dict__.__sizeof__())
pt1 = Point2D(10, 20)
print(pt1.__sizeof__())

t1 = timeit.timeit(pt.calk)   # Getting work time
t2 = timeit.timeit(pt1.calk)
print(t1, t2)





#########


"""
Коллекция __slots__
Part 2
https://stepik.org/lesson/702001/step/2?unit=702102
"""


class Point2D:
    __slots__ = ('x', 'y', '__length')   # To allow local attributes.  After that __dict__ does not exist

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__length = (x ** x + y ** y) ** 0.5

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        self.__length = value


class Point3D(Point2D):
    __slots__ = 'z'

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


pt1 = Point2D(1, 2)
print(pt1.length)

pt2 = Point3D(1, 2, 3)
pt2.z = 40


######


class Planet:
    def __init__(self, name, diametr, period_solar, period):
        self._name = name
        self._diametr = diametr
        self._period_solar = period_solar
        self._period = period


class SolarSystem:
    __slots__ = ('_mercury', '_venus', '_earth', '_mars', '_jupiter', '_saturn', '_uranus', '_neptune')
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        self._mercury = Planet('Меркурий', 4878, 87.97, 1407.5)
        self._venus = Planet('Венера', 12104, 224.7, 5832.45)
        self._earth = Planet('Земля', 12756, 365.3, 23.93)
        self._mars = Planet('Марс', 6794, 687, 24.62)
        self._jupiter = Planet('Юпитер', 142800, 4330, 9.9)
        self._saturn = Planet('Сатурн', 120660, 10753, 10.63)
        self._uranus = Planet('Уран', 51118, 30665, 17.2)
        self._neptune = Planet('Нептун', 49528, 60150, 16.1)


s_system = SolarSystem()

