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

