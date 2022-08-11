"""
Функция issubclass()
"""

class Vector(list):
    def __str__(self):
        return ' '.join(map(str, self))


v = Vector([1, 2, 3])
print(v)

########

class ListInteger(list):
    def __init__(self, nums):
        if all([type(i) == int for i in nums]):
            super().__init__(nums)
        else:
            raise TypeError('можно передавать только целочисленные значения')

    def __setitem__(self, key, value):
        self.value_checker(value)
        super().__setitem__(key, value)

    def append(self, num):
        self.value_checker(num)
        super().append(num)

    @staticmethod
    def value_checker(val):
        if type(val) != int:
            raise TypeError('можно передавать только целочисленные значения')
        return


s = ListInteger((1, 2, 3))
s[1] = 10
s.append(11)
print(s)
s[0] = 10.5 # TypeError

######


class Protists:
    def __init__(self, name, weight, old):
        self.name = name
        self.weight = weight
        self.old = old


class Plants(Protists):
    pass


class Animals(Protists):
    pass


class Mosses(Plants):
    pass


class Flowering(Plants):
    pass


class Worms(Animals):
    pass


class Mammals(Animals):
    pass


class Human(Mammals):
    pass


class Monkeys(Mammals):
    pass


class Monkey(Monkeys):
    pass


class Person(Human):
    pass


class Flower(Flowering):
    pass


class Worm(Worms):
    pass


lst_objs = [Monkey("мартышка", 30.4, 7), Monkey("шимпанзе", 24.6, 8),
            Person("Балакирев", 88, 34), Person("Верховный жрец", 67.5, 45),
            Flower("Тюльпан", 0.2, 1), Flower("Роза", 0.1, 2),
            Worm("червь", 0.01, 1), Worm("червь 2", 0.02, 1)]


lst_animals = [i for i in lst_objs if isinstance(i, Animals)]
lst_plants = [i for i in lst_objs if isinstance(i, Plants)]
lst_mammals = [i for i in lst_objs if isinstance(i, Mammals)]

print(lst_animals)
print(lst_plants)
print(lst_mammals)

