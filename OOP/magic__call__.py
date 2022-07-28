import math


class StripChars:
  """
    Магический метод __call__. Функторы и классы-декораторы
    https://stepik.org/lesson/701987/step/1?unit=702088
    """
    def __init__(self, chars):
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise TypeError("Type Error")
        return args[0].strip(self.__chars)


s1 = StripChars('?:!,; ')
s2 = StripChars(' ')
res = s1(" Hello World!  ")
res1 = s2(" Hello World!  ")
print(res)
print(res1)


class Derivate:
    def __init__(self, func):
        self.__fn = func

    def __call__(self, x, dx=0.0001, *args, **kwargs):
        return (self.__fn(x + dx) - self.__fn(x)) / dx


@Derivate
def df_sin(x):
    return math.sin(x)


#df_sin = Derivate(df_sin)
print(df_sin(math.pi/3))


### Passwords generator using__call__
import random
class RandomPassword:
    def __init__(self, psw_chars, min_length, max_length):
        self.__psw_chars = psw_chars
        self.__min_length = min_length
        self.__max_length = max_length

    def __call__(self, *args, **kwargs):
        pasw_len = random.randint(self.__min_length, self.__max_length)
        pasword = ''
        for i in range(pasw_len):
            pasword += random.choice(self.__psw_chars)
        return pasword


min_length = 5
max_length = 20
psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"
rnd = RandomPassword(psw_chars, min_length, max_length)
lst_pass = [rnd() for _ in range(3)]
print(lst_pass)


### FileAcceptor

class ImageFileAcceptor:
    def __init__(self, extensions):
        self.__extensions = extensions

    def __call__(self, *args, **kwargs):
        return True if args[0].split('.')[-1] in self.__extensions else False
      
      
filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.png"]
acceptor = ImageFileAcceptor(('jpg', 'bmp', 'jpeg'))
image_filenames = filter(acceptor, filenames)
print(list(image_filenames))  # ["boat.jpg", "ava.jpg", "forest.jpeg"]


### Form Validator

class LoginForm:
    def __init__(self, name, validators=None):
        self.name = name
        self.validators = validators
        self.login = ""
        self.password = ""

    def post(self, request):
        self.login = request.get('login', "")
        self.password = request.get('password', "")

    def is_validate(self):
        if not self.validators:
            return True

        for v in self.validators:
            if not v(self.login) or not v(self.password):
                return False

        return True


class LengthValidator:
    def __init__(self, min_length, max_length):
        self.__min_length = min_length
        self.__max_length = max_length

    def __call__(self, *args, **kwargs):
        return self.__min_length <= len(args[0]) <= self.__max_length


class CharsValidator:
    def __init__(self, chars):
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        #return set(args[0]).issubset(set(self.chars))
        for a in args:
            for i in a:
                if i not in self.__chars:
                    return False
        return True


from string import ascii_lowercase, digits


lg = LoginForm("Вход на сайт", validators=[LengthValidator(3, 50), CharsValidator(ascii_lowercase + digits)])
lg.post({"login": "root", "password": "panda"})
if lg.is_validate():
    print("Дальнейшая обработка данных формы")
    
####

class DigitRetrieve:
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        if args[0].isdigit() or args[0][1:].isdigit() and args[0][0] == '-':
            return int(args[0])
        return None

dg = DigitRetrieve()
d1 = dg("123")   # 123 (целое число)
d2 = dg("45.54")   # None (не целое число)
d3 = dg("-56")   # -56 (целое число)
d4 = dg("12fg")  # None (не целое число)
d5 = dg("abc")   # None (не целое число)

st = ["123", "abc", "-56.4", "0", "-5"]
digits = list(map(dg, st))  # [123, None, None, 0, -5]
print(digits)


####


class RenderList:
    def __init__(self, type_list):
        if type_list in ['ul', 'ol']:
            self.type_list = type_list
        else:
            self.type_list = 'ul'

    def __call__(self, lst, *args, **kwargs):
        s = f'''<{self.type_list}>\n'''
        for i in lst:
            s += f'<li>{i}</li>\n'
        return s + f'</{self.type_list}>'


lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("u")
html = render(lst)
print(html)


###


class HandlerGET:
  """
  https://stepik.org/lesson/701987/step/8?thread=solutions&unit=702088
  """
    def __init__(self, func):
        self.__fn = func

    def __call__(self, request, *args, **kwargs):
        return self.get(self.__fn, request)

    def get(self, func, request, *args, **kwargs):
        if 'method' not in request or request['method'] == 'GET':
            return f'GET: {func(request)}'
        return None


@HandlerGET
def contact(request):
    return "Сергей Балакирев"

res = contact({"method": "GET", "url": "contact.html"})
print(res)


###


class Handler:
    def __init__(self, methods=('GET',)):
        self.methods = methods

    def __call__(self, func):
        def wrapper(request, *args, **kwargs):
            if 'method' not in request or request['method'] in self.methods and request['method'] == 'GET':
                return self.get(func, request)
            elif request['method'] in self.methods and request['method'] == 'POST':
                return self.post(func, request)
            else:
                return None
        return wrapper

    def get(self, func, request, *args, **kwargs):
        if 'method' not in request or request['method'] == 'GET':
            return f'GET: {func(request)}'
        return None

    def post(self, func, request, *args, ** kwargs):
        if request['method'] == 'POST':
            return f'POST: {func(request)}'


@Handler() # по умолчанию methods = ('GET',)
def contact(request):
    return "Сергей Балакирев"

res = contact({"method": "GET", "url": "contact.html"})
print(res)


###


class InputValues:
    def __init__(self, render):     # render - ссылка на функцию или объект для преобразования
        self.render = render

    def __call__(self, func):     # func - ссылка на декорируемую функцию
        def wrapper(*args, **kwargs):
            return [self.render(i) for i in func(input()).split()]
        return wrapper


class RenderDigit:
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        if args[0].isdigit() or args[0][1:].isdigit() and args[0][0] == '-':
            return int(args[0])
        return None


@InputValues(render=RenderDigit())
def input_dg(str):
    return str

res = input_dg()
print(res)
