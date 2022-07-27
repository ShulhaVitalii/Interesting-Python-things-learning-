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
