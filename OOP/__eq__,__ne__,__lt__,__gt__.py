"""
Методы сравнений __eq__, __ne__, __lt__, __gt__ и другие
https://stepik.org/lesson/701990/step/1?unit=702091
"""

class Clock:

    __DAY = 86400  # number of seconds in one day

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError('Seconds should be integer')
        self.seconds = seconds % self.__DAY

    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError('Int Clock')

        return other if isinstance(other, int) else other.seconds

    def __eq__(self, other):   # == work for != like not(x == y)
        sc = self.__verify_data(other)
        return self.seconds == sc

    def __lt__(self, other):   # x < y  work for > like y > x
        sc = self.__verify_data(other)
        return self.seconds < sc

    def __gt__(self, other):
        sc = self.__verify_data(other)
        return self.seconds > sc

    def __le__(self, other):   # x <= y  work for >= like y >= x
        sc = self.__verify_data(other)
        return self.seconds <= sc

    def __ge__(self, other):
        sc = self.__verify_data(other)
        return self.seconds >= sc

c1 = Clock(1000)
c2 = Clock(2000)
print(c1 == c2)
print(c1 != c2)
print(c1 > c2)
print(c1 < c2)
print(c1 >= c2)
print(c1 <= c2)



#########


class Track:
    def __init__(self, start_x=0, start_y=0):
        # self.start_x = start_x
        # self.start_y = start_y
        self.track = [TrackLine(start_x, start_y)]

    def add_track(self, tr):
        self.track.append(tr)

    def get_tracks(self):
        return tuple(self.track)

    def __len__(self):
        l = 0
        for i in range(len(self.track)-1):
            l += ((self.track[i].to_x - self.track[i+1].to_x)**2 + (self.track[i].to_y - self.track[i+1].to_y)**2)**0.5

        return int(l)

    def __eq__(self, other):
        return len(self) == len(other)

    def __lt__(self, other):
        return len(self) < len(other)


class TrackLine:
    def __init__(self, to_x, to_y, max_speed=0):
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed


track1, track2 = Track(), Track(0, 1)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))
res_eq = track1 == track2
print(res_eq)
print(len(track1))
print(len(track2))


############


class Dimensions:

    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def num_checker(cls, num):
        return True if cls.MIN_DIMENSION <= num <= cls.MAX_DIMENSION else False

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, num):
        if self.num_checker(num):
            self.__a = num

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, num):
        if self.num_checker(num):
            self.__b = num

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, num):
        if self.num_checker(num):
            self.__c = num

    def get_volume(self):
        return self.a * self.b * self.c

    def __lt__(self, other):
        return self.get_volume() < other.get_volume()

    def __le__(self, other):
        return self.get_volume() <= other.get_volume()


class ShopItem:
    def __init__(self, name, price, dim):
        self.name = name
        self.price = price
        self.dim = dim


trainers = ShopItem('кеды', 1024, Dimensions(40, 30, 120))
umbrella = ShopItem('зонт', 500.24, Dimensions(10, 20, 50))
fridge = ShopItem('холодильник', 40000, Dimensions(2000, 600, 500))
chair = ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200))
lst_shop = (trainers, umbrella, fridge, chair)
lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim)

print([i.name for i in lst_shop_sorted])


#####################


stich = ["Я к вам пишу – чего же боле?",
        "Что я могу еще сказать?",
        "Теперь, я знаю, в вашей воле",
        "Меня презреньем наказать.",
        "Но вы, к моей несчастной доле",
        "Хоть каплю жалости храня,",
        "Вы не оставите меня."]


def get_list(s):
    while '  ' in s:
        s.replace('  ', ' ')
    return [i.strip('–?!,.;') for i in s.split() if i not in '–?!,.;']


stich = [get_list(i) for i in stich]


class StringText:
    def __init__(self, lst_words):
        self.lst_words = lst_words

    def __lt__(self, other):
        return len(self.lst_words) < len(other.lst_words)

    def __le__(self, other):
        return len(self.lst_words) <= len(other.lst_words)


lst_text = [StringText(s) for s in stich]
lst_text_sorted = [' '.join(i.lst_words) for i in sorted(lst_text, key=lambda x: x, reverse=True)]

print(*lst_text_sorted, sep='\n')



###########



class Morph:
    def __init__(self, *args):
        self.words = [*args]

    def add_word(self, word):
        if word not in self.words:
            self.words.append(word)

    def get_words(self):
        return tuple(self.words)

    def __eq__(self, other):
        return other.lower() in self.words


dict_words = [Morph('связь', 'связи', 'связью', 'связи', 'связей', 'связям', 'связями', 'связях'),
              Morph('формула', 'формулы', 'формуле', 'формулу', 'формулой', 'формул', 'формулам', 'формулами', 'формулах'),
              Morph('вектор', 'вектора', 'вектору', 'вектором', 'векторе', 'векторы', 'векторов', 'векторам',
                    'векторами', 'векторах'),
              Morph('эффект', 'эффекта', 'эффекту', 'эффектом', 'эффекте', 'эффекты', 'эффектов', 'эффектам',
                    'эффектами', 'эффектах'),
              Morph('день', 'дня', 'дню', 'днем', 'дне', 'дни', 'дням', 'днями', 'днях')]

text = input().strip('.').lower()
counter = 0
for i in text.split():
    for word in dict_words:
        if word == i:
            counter += 1
print(counter)



####


class CentralBank:
    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def register(cls, money):
        money.cb = cls.rates


class Money:
    def __init__(self, money=0.0):
        self.cb = None
        self.volume = money

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, cb):
        self.__cb = cb

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume):
        if type(volume) in (int, float):
            self.__volume = volume

    def volume_to_r(self):
        if type(self) == MoneyR:
            volume = self.volume * self.cb['dollar']
        elif type(self) == MoneyD:
            volume = self.volume * self.cb['rub']
        elif type(self) == MoneyE:
            volume = (self.volume / self.cb['euro']) * self.cb['rub']
        return volume

    def checker(self, one, two):
        if self.cb is None:
            raise ValueError("Неизвестен курс валют.")
        one = one.volume_to_r()
        two = two.volume_to_r()
        return one, two

    def __eq__(self, other):
        one, two = self.checker(self, other)
        return two - two * 0.1 <= one <= two + two * 0.1

    def __lt__(self, other):
        one, two = self.checker(self, other)
        return one < two

    def __le__(self, other):
        one, two = self.checker(self, other)
        return one <= two


class MoneyR(Money):
    pass


class MoneyD(Money):
    pass


class MoneyE(Money):
    pass



cb = CentralBank()
print(cb)   # None

CentralBank.rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

r = MoneyR(50000)
d = MoneyD(800)
e = MoneyE(500)

assert r.volume == 50000 and d.volume == 800 and e.volume == 500, "атрибут volume в кошельках принимает неверное значение"

CentralBank.register(r)
CentralBank.register(d)
CentralBank.register(e)
print(r.volume)
assert r.volume == 50000 and d.volume == 800 and e.volume == 500, "атрибут volume в кошельках принимает неверное значение"
assert d > r and e < d, "неверно отработали операторы сравнения > и <"

d1 = MoneyD(800)
d2 = MoneyD(800.005)
CentralBank.register(d1)
CentralBank.register(d2)
assert d1 == d2, "оператор == вернул False при значениях средств 800 и 800.0005 в кошельках"

