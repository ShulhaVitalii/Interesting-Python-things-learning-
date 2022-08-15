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
