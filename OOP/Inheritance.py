"""
https://stepik.org/lesson/701995/step/5?unit=702096
"""

class Animal:
    def __init__(self, name, old):
        self.name = name
        self.old = old


class Cat(Animal):
    def __init__(self, name, old, color, weight):
        super().__init__(name, old)
        self.color = color
        self.weight = weight

    def get_info(self):
        return f'{self.name}: {self.old}, {self.color}, {self.weight}'


class Dog(Animal):
    def __init__(self, name, old, breed, size):
        super().__init__(name, old)
        self.breed = breed
        self.size = size

    def get_info(self):
        return f'{self.name}: {self.old}, {self.breed}, {self.size}'

cat = Cat('кот', 4, 'black', 2.25)
print(cat.get_info())


##########


class Thing:
    num = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Thing.num += 1
        self.id = Thing.num
        self.weight = self.dims = self.memory = self.frm = None

    def get_data(self):
        return (self.id, self.name, self.price, self.weight, self.dims, self.memory, self.frm)


class Table(Thing):
    def __init__(self, name, price, weight, dims):
        super().__init__(name, price)
        self.weight = weight
        self.dims = dims


class ElBook(Thing):
    def __init__(self, name, price, memory, frm):
        super().__init__(name, price)
        self.memory = memory
        self.frm = frm

table = Table("Круглый", 1024, 812.55, (700, 750, 700))
book = ElBook("Python ООП", 2000, 2048, 'pdf')
print(*table.get_data())
print(*book.get_data())


##########


class GenericView:
    def __init__(self, methods=('GET',)):
        self.methods = methods

    def get(self, request):
        return ""

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass


class DetailView(GenericView):
    def __init__(self, methods=None):
        if methods is None:
            super().__init__()
        else:
            self.methods = methods

    def render_request(self, request, method):
        if method.upper() not in self.methods:
            raise TypeError('данный запрос не может быть выполнен')
        d = {'get': self.get, 'post': self.post, 'put': self.put, 'delete': self.delete}
        result = d[method.lower()](request)

        return result

        # One more possible solution

        # df = getattr(self, method.lower())
        # self.get(request)
        # return df(request)

    def get(self, request):
        if type(request) != dict:
            raise TypeError('request не является словарем')
        if 'url' not in request:
            raise TypeError('request не содержит обязательного ключа url')

        return f'url: {request["url"]}'



dv = DetailView(methods=('GET', 'POST'))
html = dv.render_request({'url': 'https://site.ru/home'}, 'GET')
print(html)



###########


class Validator:
    """
    https://stepik.org/lesson/701995/step/9?thread=solutions&unit=702096
    """
    def _is_valid(self, data):
        return True

    def __call__(self, data, *args, **kwargs):
        if not self._is_valid(data):
            raise ValueError('данные не прошли валидацию')
        return True


class IntegerValidator(Validator):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data):
        if type(data) == int and self.min_value <= data <= self.max_value:
            return True
        return False


class FloatValidator(Validator):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data):
        if type(data) == float and self.min_value <= data <= self.max_value:
            return True
        return False

v = Validator()
v(4)
integer_validator = IntegerValidator(-10, 10)
float_validator = FloatValidator(-1, 1)
res1 = integer_validator(10)  # True
print(res1)
res2 = float_validator(10)    # исключение ValueError


########


"""
Используя механизм наследования, вам поручено разработать функционал по построению моделей нейронных сетей...
https://stepik.org/lesson/701995/step/10?unit=702096
https://youtu.be/I8upOO_ZjqQ
"""

class Layer:
    def __init__(self, name='Layer'):
        self.next_layer = None
        self.name = name

    def __call__(self, layer, *args, **kwargs):
        self.next_layer = layer
        return layer


class Input(Layer):
    def __init__(self, inputs):
        super().__init__('Input')
        self.inputs = inputs


class Dense(Layer):
    def __init__(self, inputs, outputs, activation):
        super().__init__('Dense')
        self.inputs = inputs
        self.outputs = outputs
        self.activation = activation


class NetworkIterator:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        layer = self.start
        while layer:
            yield layer
            layer = layer.next_layer


nt = Input(12)
layer = nt(Dense(nt.inputs, 1024, 'relu'))
layer = layer(Dense(layer.inputs, 2048, 'relu'))
layer = layer(Dense(layer.inputs, 10, 'softmax'))

n = 0
for x in NetworkIterator(nt):
    assert isinstance(x, Layer), "итератор должен возвращать объекты слоев с базовым классом Layer"
    n += 1

assert n == 4, "итератор перебрал неверное число слоев"



############



class Vector:
    def __init__(self, *args):
        self.coords = [*args]

    def get_coords(self):
        return tuple(self.coords)

    def __add__(self, other):
        if len(self.get_coords()) != len(other.get_coords()):
            raise TypeError('размерности векторов не совпадают')
        res = []
        for i in range(len(self.coords)):
            res.append(self.coords[i] + other.coords[i])
        if all([type(i) == int for i in res]):
            return self.__class__(*res)
        return self.__class__.__base__(*res)

    def __sub__(self, other):
        if len(self.coords) != len(other.coords):
            raise TypeError('размерности векторов не совпадают')
        res = []
        for i in range(len(self.coords)):
            res.append(self.coords[i] - other.coords[i])
        if all([type(i) == int for i in res]):
            return __class__(*res)
        return __class__.__base__(*res)


class VectorInt(Vector):
    def __init__(self, *args):
        if all([type(i) == int for i in args]):
            super().__init__(*args)
        else:
            raise ValueError('координаты должны быть целыми числами')





v1 = Vector(1, 2, 3)
v2 = Vector(3, 4, 5)

assert (v1 + v2).get_coords() == (
4, 6, 8), "операция сложения дала неверные значения (или некорректно работает метод get_coords)"
assert (v1 - v2).get_coords() == (
-2, -2, -2), "операция вычитания дала неверные значения (или некорректно работает метод get_coords)"

v = VectorInt(1, 2, 3, 4)
assert isinstance(v, Vector), "класс VectorInt должен наследоваться от класса Vector"

try:
    v = VectorInt(1, 2, 3.4, 4)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError для команды v = VectorInt(1, 2, 3.4, 4)"

v1 = VectorInt(1, 2, 3, 4)
v2 = VectorInt(4, 2, 3, 4)
v3 = Vector(1.0, 2, 3, 4)

v = v1 + v2
assert type(
    v) == VectorInt, "при сложении вектором с целочисленными координатами должен формироваться объект класса VectorInt"
v = v1 + v3
assert type(v) == Vector, "при сложении вектором с вещественными координатами должен формироваться объект класса Vector"



#########


class Tuple(tuple):
    def __init__(self, iter_obj):
        self.iter_obg = tuple(i for i in iter_obj)

    def __add__(self, other):
        other = tuple(i for i in other)
        return Tuple(self.iter_obg + other)


t = Tuple([1, 2, 3])
t = t + "Python"
print(t)   # (1, 2, 3, 'P', 'y', 't', 'h', 'o', 'n')
t = (t + "Python") + "ООП"
print(t)

