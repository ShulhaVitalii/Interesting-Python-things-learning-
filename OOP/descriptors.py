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


#######################


class ValidateString:
    def __init__(self, min_length=3, max_length=100):
        self.min = min_length
        self.max = max_length

    def validate(self, string):
        if type(string) == str:
            if self.min <= len(string) <= self.max:
                return True
        return False


class StringValue:
    def __init__(self, validator):
        self.validator = validator

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.validator.validate(value):
            setattr(instance, self.name, value)


class RegisterForm:
    login = StringValue(validator=ValidateString())
    password = StringValue(validator=ValidateString())
    email = StringValue(validator=ValidateString())

    def __init__(self, login, password, email):
        self.login = login
        self.password = password
        self.email = email

    def get_fields(self):
        return [self.login, self.password, self.email]

    def show(self):
        print(
            f"""
            <form>
            Логин: {self.login}
            Пароль: {self.password}
            Email: {self.email}
            </form>
            """)

f = RegisterForm('Loggg', 'password', 'email')
f.show()


#######################

class PriceValue:
    def __init__(self, max_value=10000):
        self.max_value = max_value

    def validate_value(self, value):
        if type(value) == int or type(value) == float:
            if value <= self.max_value:
                return True
        return False

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.validate_value(value):
            setattr(instance, self.name, value)


class StringValue:
    def __init__(self, min_length=2, max_length=50):
        self.min = min_length
        self.max = max_length

    def validate_value(self, value):
        if type(value) == str:
            if self.min <= len(value) <= self.max:
                return True
        return False

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.validate_value(value):
            setattr(instance, self.name, value)


class SuperShop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


class Product:
    name = StringValue()
    price = PriceValue()

    def __init__(self, name, price):
        self.name = name
        self.price = price


shop = SuperShop("У Балакирева")
shop.add_product(Product("Курс по Python", 0))
shop.add_product(Product("Курс по Python ООП", 2000))
for p in shop.goods:
    print(f"{p.name}: {p.price}")

x = Product('Опа', 100)
shop.add_product(x)
shop.remove_product(x)



#####


class Nums:
    @classmethod
    def verify_num(cls, coord):
        if type(coord) not in [int, float] or coord <= 0:
            raise ValueError("длины сторон треугольника должны быть положительными числами")

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_num(value)
        setattr(instance, self.name, value)


class Triangle:
    a = Nums()
    b = Nums()
    c = Nums()

    def __init__(self, a, b, c):
        if a < b+c and b < a+c and c < a+b:
            self.a = a
            self.b = b
            self.c = c
        else:
            raise ValueError("с указанными длинами нельзя образовать треугольник")

    def __len__(self):
        return int(self.a + self.b + self.c)

    def __call__(self, *args, **kwargs):
        p = len(self)/2
        s = (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
        return s


tr = Triangle(5, 4, 3)
assert tr.a == 5 and tr.b == 4 and tr.c == 3, "дескрипторы вернули неверные значения"

try:
    tr = Triangle(-5, 4, 3)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    tr = Triangle(10, 1, 1)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

tr = Triangle(5, 4, 3)
assert len(tr) == 12, "функция len вернула неверное значение"
assert 5.9 < tr() < 6.1, "метод __call__ вернул неверное значение"

