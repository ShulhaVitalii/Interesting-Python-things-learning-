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


