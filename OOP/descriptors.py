## Data descriptor
class Integer:
    """
    Дескрипторы (data descriptor и non-data descriptor)
    https://stepik.org/lesson/701985/step/1?unit=702086
    """
    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError('Coord should be integer')
            
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_coord(value)
        setattr(instance, self.name, value)


class Point3D:
    x = Integer()
    y = Integer()
    z = Integer()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


p = Point3D(1, 2, 3)
print(p.__dict__)


######### Non Data descriptor

class ReadIntX: #Non-data descriptor
    def __set_name__(self, owner, name):
        self.name = "_x"

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


class Integer: # Data descriptor
    """
    https://stepik.org/lesson/701985/step/1?unit=702086
    """
    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError('Coord should be integer')

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)#instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.verify_coord(value)
        setattr(instance, self.name, value)


class Point3D:
    x = Integer()
    y = Integer()
    z = Integer()
    xr = ReadIntX()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


p = Point3D(1, 2, 3)
p.xr = 5
print(p.xr, p.__dict__, p.z)

