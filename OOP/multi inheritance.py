# mixins
# multi inheritance
# MRO - Method Resolution Order


class Goods:
    def __init__(self, name, weight, price):
        super().__init__()   # for call init in MixinLog
        print('Init Goods')
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f'{self.name}, {self.weight}, {self.price}')


class MixinLog:
    ID = 0

    def __init__(self):
        print('Init MixinLog')
        self.ID += 1
        self.id = self.ID

    def save_sell_log(self):
        print(f'{self.id}: sell in 00:00')

    def print_info(self):
        print(f'print_info from MixinLog')


class NoteBook(Goods, MixinLog):
    pass


n = NoteBook('Acer', 1.5, 30000)
n.print_info()
n.save_sell_log()

print(NoteBook.__mro__)

MixinLog.print_info(n)



######


class Digit:
    def __init__(self, value):
        self.checking_value(value)
        self.value = value

    def checking_value(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('значение не соответствует типу объекта')


class Integer(Digit):
    def checking_value(self, value):
        super().checking_value(value)
        if type(value) != int:
            raise TypeError('значение не соответствует типу объекта')


class Float(Digit):
    def checking_value(self, value):
        super().checking_value(value)
        if type(value) != float:
            raise TypeError('значение не соответствует типу объекта')


class Positive(Digit):
    def checking_value(self, value):
        super().checking_value(value)
        if value <= 0:
            raise TypeError('значение не соответствует типу объекта')


class Negative(Digit):
    def checking_value(self, value):
        super().checking_value(value)
        if value >= 0:
            raise TypeError('значение не соответствует типу объекта')


class PrimeNumber(Integer, Positive):
    pass


class FloatPositive(Float, Positive):
    pass


digits = [PrimeNumber(3), PrimeNumber(1), PrimeNumber(4), FloatPositive(1.5), FloatPositive(9.2), FloatPositive(6.5),
          FloatPositive(3.5), FloatPositive(8.9)]

lst_positive = [i for i in digits if isinstance(i, Positive)]
lst_float = [i for i in digits if isinstance(i, Float)]

