from functools import wraps
import math


# Декоратор функции с параметрами
def df_decorator(dx=0.01):
    def func_decorator(func):
        @wraps(func)
        def wrapper(x, *args, **kwargs):
            res = (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
            return res

            # wrapper.__name__ = func.__name__
            # wrapper.__doc__ = func.__doc__

        return wrapper

    return func_decorator


@df_decorator(dx=0.01)
def sin_df(x):
    """ Функция для вычисления производной синуса """
    return math.sin(x)

sin_df = df_decorator(dx=0.001)(sin_df)

df = sin_df(math.pi / 3)

print(df)
print(sin_df.__name__)
print(sin_df.__doc__)





######


def integer_params_decorated(func):
    def wrapper(self, *args, **kwargs):
        for i in args:
            if type(i) != int:
                raise TypeError("аргументы должны быть целыми числами")

        if not all(type(x) == int for x in kwargs.values()):
            raise TypeError("аргументы должны быть целыми числами")

        return func(self, *args, **kwargs)
    return wrapper


def integer_params(cls):
    methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
    for k, v in methods.items():
        setattr(cls, k, integer_params_decorated(v))

    return cls


@integer_params
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value

    def set_coords(self, *coords, reverse=False):
        c = list(coords)
        self.__coords = c if not reverse else c[::-1]


vector = Vector(1, 2)
print(vector[1])
vector[1] = 20.4 # TypeError
