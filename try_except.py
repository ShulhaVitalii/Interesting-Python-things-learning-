def get_number(x):
    try:
        return int(x)
    except:
        try:
            return float(x)
        except:
            return x

res_1 = get_number('-5')
res_2 = get_number('5.78')
res_3 = get_number('8(912)000-000-00')
print(res_1)
print(res_2)
print(res_3)


########

class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y


pt = Point(1, 2)

try:
    print(pt.z)
except AttributeError:
    print("Атрибут с именем z не существует")
    
    
    #########

lst_in = input().split()


def is_int(num):
    try:
        num = int(num)
        return True
    except ValueError:
        return False


s = sum(map(int, filter(is_int, lst_in)))

# s = 0
#
# for i in lst_in:
#     if is_int(i):
#         s += int(i)
print(s)
# <= 8 11 abcd -7.5 2.0 -5
# => 14


##########

lst_in = input().split()


def convert(num):
    try:
        num = int(num)
        return num
    except ValueError:
        try:
            num = float(num)
            return num
        except ValueError:
            return num


lst_out = [convert(i) for i in lst_in]
print(lst_out)


#########

class Triangle:

    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise TypeError('стороны треугольника должны быть положительными числами')
        if a+b < c or b+c < a or c+a < b:
            raise ValueError('из указанных длин сторон нельзя составить треугольник')
        self._a = a
        self._b = b
        self._c = c


input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5), (7, 4, 6)]

lst_tr = []
for i in input_data:
    try:
        lst_tr.append(Triangle(*i))
    except TypeError:
        pass
    except ValueError:
        pass
print(lst_tr)

######


class FloatValidator:

    def __init__(self, min_value, max_value):
        self._min = min_value
        self._max = max_value

    def __call__(self, value, *args, **kwargs):
        if type(value) != float or value > self._max or value < self._min:
            raise ValueError('значение не прошло валидацию')


class IntegerValidator:

    def __init__(self, min_value, max_value):
        self._min = min_value
        self._max = max_value

    def __call__(self, value, *args, **kwargs):
        if type(value) != int or value > self._max or value < self._min:
            raise ValueError('значение не прошло валидацию')


def is_valid(lst, validators):
    res = []
    for value in lst:
        for validator in validators:
            try:
                validator(value)
                res.append(value)
            except:
                pass
    return res


fv = FloatValidator(0, 10.5)
iv = IntegerValidator(-10, 20)

lst_out = is_valid([1, 4.5, -10.5, 100, True, 'abc', (1, 2)], validators=[fv, iv])  # [1, 4.5]
print(lst_out)


#######

# Блоки finally и else

try:
    x, y = map(int, input().split())
    res = x / y
except ZeroDivisionError as p:
    print(p)
except ValueError as p:
    print(p)
else:
    print('There are did not been exceptions')
finally:
    print('You always ben see message from finally')

#######

def get_values():
    try:
        x, y = map(int, input().split())
        return x, y
    except ValueError as p:
        print(p)
        return 0, 0
    finally:
        print('finally return before "return"!!!')

x, y = get_values()
print(x,y)


#####

x, y = input().split()
try:
    res = int(x)+int(y)
except ValueError:
    try:
        res = float(x) + float(y)
    except ValueError:
        res = x + y
finally:
    print(res)


######


class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y


x, y = input().split()
try:
    pt = Point(int(x), int(y))
except ValueError:
    try:
       pt = Point(float(x), float(y))
    except ValueError:
        try:
            pt = Point()
        except:
            pass
finally:
    print(f"Point: x = {pt._x}, y = {pt._y}")
    
    
    ########
    

def get_loss(w1, w2, w3, w4):
    try:
        w1 // w2
    except ZeroDivisionError:
        return "деление на ноль"
    else:
        y = 10 * w1 // w2 - 5 * w2 * w3 + w4
        return y

c = get_loss(1,0,3,4)
print(c)


###########


class Rect:
    def __init__(self, x, y, width, height):
        if type(x) not in (int, float) or type(y) not in (int, float) or width <= 0 or height <= 0:
            raise ValueError('некорректные координаты и параметры прямоугольника')
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def is_collision(self, rect):
        a = {i for i in range(self._x, self._width + self._x + 1)}
        b = {i for i in range(self._y - self._height, self._y + 1)}
        c = {i for i in range(rect._x, rect._width + rect._x + 1)}
        d = {i for i in range(rect._y - rect._height, rect._y + 1)}
        if len(a & c) == 0 or len(b & d) == 0:
            return True
        else:
            raise TypeError('прямоугольники пересекаются')



lst_rect = [Rect(0, 0, 5, 3), Rect(6, 0, 3, 5), Rect(3, 2, 4, 4), Rect(0, 8, 8, 1)]
lst_not_collision = []


for rect in lst_rect:
    try:
        for i in lst_rect:
            if i != rect:
                rect.is_collision(i)
        lst_not_collision.append(rect)
    except TypeError:
        pass

r = Rect(1, 2, 10, 20)
assert r._x == 1 and r._y == 2 and r._width == 10 and r._height == 20, "неверные значения атрибутов объекта класса Rect"

r2 = Rect(1.0, 2, 10.5, 20)

try:
    r2 = Rect(0, 2, 0, 20)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при создании объекта Rect(0, 2, 0, 20)"


assert len(lst_rect) == 4, f"список lst_rect содержит не 4 элемента, {len(lst_rect)}"
assert len(lst_not_collision) == 1, f"неверное число элементов в списке lst_not_collision {len(lst_not_collision)}"

def not_collision(rect):
    for x in lst_rect:
        try:
            if x != rect:
                rect.is_collision(x)
        except TypeError:
            return False
    return True

f = list(filter(not_collision, lst_rect))
assert lst_not_collision == f, "неверно выделены не пересекающиеся прямоугольники, возможно, некорректно работает метод is_collision"

r = Rect(3, 2, 2, 5)
rr = Rect(1, 4, 6, 2)

try:
    r.is_collision(rr)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError при вызове метода is_collision() для прямоугольников Rect(3, 2, 2, 5) и Rect(1, 4, 6, 2)"


#########

class ValidatorString:
    def __init__(self, min_length, max_length, chars):
        self._min = min_length
        self._max = max_length
        self.chars = chars

    def is_valid(self, string):
        if self.chars == '':
            return

        # if self._min > len(string) or len(string) > self._max:
        if self._max < len(string) < self._min:
            raise ValueError('недопустимая строка')

        for i in self.chars:
            if i in string:
                return
        raise ValueError('недопустимая строка')


class LoginForm:
    def __init__(self, login_validator, password_validator):
        self.lv = login_validator
        self.pv = password_validator
        self._login = self._password = None

    def form(self, request):
        if 'login' not in request or 'password' not in request:
            raise TypeError('в запросе отсутствует логин или пароль')

        self.lv.is_valid(request['login'])
        self.pv.is_valid(request['password'])
        self._login = request['login']
        self._password = request['password']


login_v = ValidatorString(4, 50, "")
password_v = ValidatorString(10, 50, "!$#@%&?")
lg = LoginForm(login_v, password_v)
login, password = input().split()
try:
    lg.form({'login': login, 'password': password})
except (TypeError, ValueError) as e:
    print(e)
else:
    print(lg._login)

    
    
    ##########
    
    
    
class Test:
    def __init__(self, descr):
        if 10 <= len(descr) <= 10000:
            self._descr = descr
        else:
            raise ValueError('формулировка теста должна быть от 10 до 10 000 символов')

    def run(self):
        raise NotImplementedError('должен быть переопределен в дочернем классе')


class TestAnsDigit(Test):
    def __init__(self, descr, ans_digit, max_error_digit=0.01):
        super().__init__(descr)
        if type(ans_digit) in (int, float) and type(max_error_digit) in (int, float) and max_error_digit > 0:
            self.ans_digit = ans_digit
            self.max_error_digit = max_error_digit
        else:
            raise ValueError('недопустимые значения аргументов теста')


    def run(self):
        ans = float(input())
        if self.ans_digit + self.max_error_digit >= ans >= self.ans_digit:
            return True
        return False


descr, ans = map(str.strip, input().split('|'))  # например: Какое значение получится при вычислении 2+2? | 4
ans = float(ans) # здесь для простоты полагаем, что ans точно число и ошибок в преобразовании быть не может
try:
    t = TestAnsDigit(descr, ans)
    print(t.run())
except ValueError as v:
    print(v)

# try:
#     test = Test('descr')
# except ValueError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение ValueError при вызове инициализатора класса Test с неверным набором аргументов"
# 
# try:
#     test = Test('descr ghgfhgjg ghjghjg')
#     test.run()
# except NotImplementedError:
#     assert True
# else:
#     assert False
# 
# assert issubclass(TestAnsDigit, Test)
# 
# t = TestAnsDigit('ffhgfh fghfghfghfggfhfghfh', 1)
# t = TestAnsDigit('ffhgfh fghfghfghfggfhfghfh', 1, 0.5)
# 
# try:
#     t = TestAnsDigit('ffhgfh fghfghfghfggfhfghfh', 1, -0.5)
# except ValueError:
#     assert True
# else:
#     assert False



###########



class TupleLimit(tuple):

    def __new__(cls, lst, max_length, *args, **kwargs):
        if len(lst) > max_length:
            raise ValueError('число элементов коллекции превышает заданный предел')
        return super().__new__(cls, lst)

    def __init__(self, lst, max_length):
        self.lst = [str(i) for i in lst]
        self._max = max_length

    def __str__(self):
        return ' '.join(self.lst)


digits = list(map(float, input().split()))
try:
    t = TupleLimit(digits, max_length=5)
    print(t)
except ValueError as v:
    print(v)
    
    
