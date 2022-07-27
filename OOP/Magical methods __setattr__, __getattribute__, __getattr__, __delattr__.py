class Point:
  """
  https://stepik.org/lesson/701986/step/1?unit=702087
  Magical methods __setattr__, __getattribute__, __getattr__, __delattr__
  """
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y

    # Using to manage access to the attribute
    def __getattribute__(self, item):
        if item == 'x':
            raise ValueError('Access denied')
        else:
            return object.__getattribute__(self, item)

    # Using to deny creation of local attribute in the class instance
    def __setattr__(self, key, value):
        if key == 'z':
            raise AttributeError('Wrong attribute name')
        object.__setattr__(self, key, value)

    # Using if the attribute is not exist
    def __getattr__(self, item):
        return False

    # Using for deletion the attribute
    def __delattr__(self, item):
        object.__delattr__(self, item)


pt1 = Point(1, 2)
pt2 = Point(10, 20)
a = pt1.y
#pt1.z = 5  # => AttributeError: Wrong attribute name
print(a)


### Examples

class Book:
    def __init__(self, title='', author='', pages=0, year=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value):
        if key in ['title', 'author']:
            if type(value) != str:
                raise TypeError("Неверный тип присваиваемых данных.")
        if key in ['pages', 'year']:
            if type(value) != int:
                raise TypeError("Неверный тип присваиваемых данных.")
        object.__setattr__(self, key, value)


book = Book('Python ООП', 'Сергей Балакирев', 123, 2022)

###

class Shop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):

        self.goods.remove(product)


class Product:
    id = 1

    def __init__(self, name, weight, price):
        self.id = self.id
        self.increase_id()
        self.name = name
        self.weight = weight
        self.price = price

    @classmethod
    def increase_id(cls):
        cls.id += 1

    def __setattr__(self, key, value):
        if key == 'name':
            if type(value) != str:
                raise TypeError("Неверный тип присваиваемых данных.")
        if key in ['weight', 'price']:
            if type(value) not in [int, float] or value <=0:
                raise TypeError("Неверный тип присваиваемых данных.")
        if key == 'id':
            if type(value) != int:
                raise TypeError("Неверный тип присваиваемых данных.")
        object.__setattr__(self, key, value)

    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")
        object.__delattr__(self, item)


shop = Shop("Балакирев и К")
book = Product("Python ООП", 0, 1024)
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))
shop.remove_product(book)
for p in shop.goods:
    print(f"{p.id}, {p.name}, {p.weight}, {p.price}")
    
