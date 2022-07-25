
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    old = property(get_age, set_age)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
    
    @name.deleter
    def name(self):
        del self.__name


p = Person('Vitalii', 30)
p.old = 31
p.name = 'Vital'
print(p.old, p.name)


class Car:
    def __init__(self):
        self.__model = ''

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if type(model) is str and 1 < len(model) < 101:
            self.__model = model


car = Car()
car.model = "Toyota"
car.model = "T"
print(car.model)



class WindowDlg:
    def __init__(self, title: str, width, height):
        self.__title = title
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if self.check_size(width):
            self.__width = width
            self.show()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if self.check_size(height):
            self.__height = height
            self.show()

    @staticmethod
    def check_size(size):
        return True if size in range(1, 10001) else False

    def show(self):
        print(f"{self.__title}: {self.__width}, {self.__height}")

uno = WindowDlg("First ", 100, 500)
uno.width = 10



class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x=0, y=0):
        self.__x = x if self.check_size(x) else 0
        self.__y = y if self.check_size(y) else 0

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if self.check_size(x):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if self.check_size(y):
            self.__y = y

    def check_size(self, size):
        if type(size) is int or type(size) is float:
            if self.MIN_COORD <= size <= self.MAX_COORD:
                return True
        else:
            return False

    @staticmethod
    def norm2(vector):
        return vector.x ** 2 + vector.y ** 2



v1 = RadiusVector2D()
v2 = RadiusVector2D(1)
v3 = RadiusVector2D(-102, 1024)

r3 = RadiusVector2D(4, 5)
print(v1.x, v1.y)
print(v2.x, v2.y)
print(v3.x, v3.y)
print(RadiusVector2D.norm2(r3))


