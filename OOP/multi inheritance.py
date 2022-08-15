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


#######


class ShopItem:
    ID_SHOP_ITEM = 0

    def __init__(self):
        super().__init__()
        ShopItem.ID_SHOP_ITEM += 1
        self._id = ShopItem.ID_SHOP_ITEM

    def get_pk(self):
        return self._id


class ShopGenericView:
    def __str__(self):
        s = (f'{k}: {v}' for k, v in self.__dict__.items())
        return '\n'.join(s)

    def __repr__(self):
        s = (f'{k}: {v}' for k, v in self.__dict__.items())
        return '\n'.join(s)


class ShopUserView:
    def __str__(self):
        s = (f'{k}: {v}' for k, v in self.__dict__.items() if k != '_id')
        return '\n'.join(s)

    def __repr__(self):
        s = (f'{k}: {v}' for k, v in self.__dict__.items() if k != '_id')
        return '\n'.join(s)


class Book(ShopItem, ShopUserView):
    def __init__(self, title, author, year):
        super().__init__()
        self._title = title
        self._author = author
        self._year = year


book = Book("Python ООП", "Балакирев", 2022)
print(book)


###########


class MoneyOperators:
    def __add__(self, other):
        if type(other) in (int, float):
            return self.__class__(self.money + other)

        if type(self) != type(other):
            raise TypeError('Разные типы объектов')

        return self.__class__(self.money + other.money)

    def __sub__(self, other):
        if type(other) in (int, float):
            return self.__class__(self.money - other)

        if type(self) != type(other):
            raise TypeError('Разные типы объектов')

        return self.__class__(self.money - other.money)


class Money:
    def __init__(self, value):
        self.money = value

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, value):
        if type(value) not in (int, float):
            raise TypeError('сумма должна быть числом')
        self._money = value


class MoneyR(Money, MoneyOperators):
    def __str__(self):
        return f"MoneyR: {self.money}"


class MoneyD(Money, MoneyOperators):
    def __str__(self):
        return f"MoneyD: {self.money}"


m1 = MoneyR(1)
m2 = MoneyD(2)
m = m1 + 10
print(m)  # MoneyR: 11
m = m1 - 5.4
m = m1 + m2  # TypeError
