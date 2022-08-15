from abc import ABC, abstractmethod

"""
https://stepik.org/lesson/701999/step/7?unit=702100

abstractmethod - using for mandatory override a method in a child class. Else raise error like 'TypeError: Can't 
instantiate abstract class ModelForm with abstract method get_pk'

Подвиг 6 (про модуль abc). В языке Python есть еще один распространенный способ объявления абстрактных методов класса
через декоратор abstractmethod модуля abc:

Чтобы корректно работал декоратор abstractmethod сам класс должен наследоваться от базового класса ABC. Например, так:
class Transport(ABC):
    @abstractmethod
    def go(self):
        'Метод для перемещения транспортного средства'

    @classmethod
    @abstractmethod
    def abstract_class_method(cls):
        'Абстрактный метод класса'
"""


class Model(ABC):
    @abstractmethod
    def get_pk(self):
        pass

    def get_info(self):
        return "Базовый класс Model"


class ModelForm(Model):
    uniq_num = 0

    def __init__(self, login, password):
        self._id = self.__get_id()
        self._login = login
        self._password = password

    @classmethod
    def __get_id(cls):
        cls.uniq_num += 1
        return cls.uniq_num

    def get_pk(self):
        return self._id


form = ModelForm("Логин", "Пароль")
print(form.get_pk())


#########


"""
https://stepik.org/lesson/701999/step/9?unit=702100

abstractmethod - using for mandatory override a method in a child class. Else raise error like 'TypeError: Can't 
instantiate abstract class ModelForm with abstract method get_pk'

Подвиг 8. С помощью модуля abc можно определять не только абстрактные методы, но и абстрактные объекты-свойства
 (property). Делается это следующим образом:

from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def go(self):
        'Метод для перемещения транспортного средства'

    @property
    @abstractmethod
    def speed(self):
        'Абстрактный объект-свойство'
"""


class CountryInterface(ABC):
    @property
    @abstractmethod
    def name(self):
        return

    @property
    @abstractmethod
    def population(self):
        return

    @property
    @abstractmethod
    def square(self):
        return

    @abstractmethod
    def get_info(self):
        return


class Country(CountryInterface):

    def __init__(self, name, population, square):
        self.name = name
        self.population = population
        self.square = square

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, population):
        self.__population = population

    @property
    def square(self):
        return self.__square

    @square.setter
    def square(self, square):
        self.__square = square

    def get_info(self):
        return f"{self.name}: {self.square}, {self.population}"


country = Country("Orkostan", 140000000, 324005489.55)
name = country.name
pop = country.population
country.population = 150000000
country.square = 354005483.0
print(country.get_info())  # Orkostan: 354005483.0, 150000000
