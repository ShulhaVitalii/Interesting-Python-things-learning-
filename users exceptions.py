class StringException(Exception):
    pass


class NegativeLengthString(StringException):
    """ошибка, если длина отрицательная"""


class ExceedLengthString(StringException):
    """ошибка, если длина превышает заданное значение"""


try:
    raise ExceedLengthString
except NegativeLengthString:
    print("NegativeLengthString")
except ExceedLengthString:
    print("ExceedLengthString")
except StringException:
    print("StringException")
    

    
##########


class PrimaryKeyError(Exception):
    def __init__(self, **kwargs):
        self.key = None
        if kwargs:
            self.key = list(kwargs.keys())[0]
            self.val = kwargs[self.key]

    def __str__(self):
        if self.key is None:
            return f'Первичный ключ должен быть целым неотрицательным числом'
        else:
            return f'Значение первичного ключа {self.key} = {self.val} недопустимо'


try:
    raise PrimaryKeyError(id=-10.5)
except PrimaryKeyError as e:
    print(e)

assert issubclass(PrimaryKeyError, Exception), "класс PrimaryKeyError должен наследоваться от класса Exception"

e1 = PrimaryKeyError(id=1)
e2 = PrimaryKeyError(pk=2)
e3 = PrimaryKeyError()

assert str(e1) == "Значение первичного ключа id = 1 недопустимо", "неверное сообщение для исключения объекта класса PrimaryKeyError"
assert str(e2) == "Значение первичного ключа pk = 2 недопустимо", "неверное сообщение для исключения объекта класса PrimaryKeyError"
assert str(e3) == "Первичный ключ должен быть целым неотрицательным числом", "неверное сообщение для исключения объекта класса PrimaryKeyError"


#######


class DateError(Exception):
    pass


class DateString:
    def __init__(self, date_string):
        self.check_data(date_string)
        self.date_string = date_string

    @staticmethod
    def check_data(data):
        d = data.split('.')
        day = int(d[0])
        month = int(d[1])
        year = int(d[2])

        if len(d) != 3 or 0 >= day or day > 31 or 0 >= month or month > 12 or 0 >= year or year > 3000:
            raise DateError('Wrong data format')

    def __str__(self):
        d = self.date_string.split('.')
        return f"{int(d[0]):02}.{int(d[1]):02}.{int(d[2]):04}"


date_string = input()
try:
    date = DateString(date_string)
    print(date)
except DateError:
    print("Неверный формат даты")
    
    
##########



class CellException(Exception):
    pass


class CellIntegerException(CellException):
    """Exception for CellInteger objects"""


class CellFloatException(CellException):
    """Exception for CellFloat objects"""


class CellStringException(CellException):
    """Exception for CellString objects"""


class CellInteger:
    def __init__(self, min_value, max_value):
        self._min_value = min_value
        self._max_value = max_value
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if self._min_value <= value <= self._max_value:
            self.__value = value
        else:
            raise CellIntegerException('значение выходит за допустимый диапазон')


class CellFloat:
    def __init__(self, min_value, max_value):
        self._min_value = min_value
        self._max_value = max_value
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if self._min_value <= value <= self._max_value:
            self.__value = value
        else:
            raise CellFloatException('значение выходит за допустимый диапазон')


class CellString:
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if self.min_length <= len(value) <= self.max_length:
            self.__value = value
        else:
            raise CellStringException('длина строки выходит за допустимый диапазон')


class TupleData:
    def __init__(self, *args):
        self.__checking_args(args)
        self.cells = [*args]

    def __checking_args(self, args):
        if all(map(lambda x: type(x) in (CellInteger, CellFloat, CellString), args)):
            return
        else:
            raise Exception('Value error')

    def __getitem__(self, item):
        if 0 <= item <= len(self.cells):
            return self.cells[item].value
        else:
            raise IndexError

    def __setitem__(self, key, value):
        if 0 <= key <= len(self.cells):
            self.cells[key].value = value
            return self
        else:
            raise IndexError

    def __len__(self):
        return len(self.cells)

    def __iter__(self):
        for i in self.cells:
            yield i.value
            
            
