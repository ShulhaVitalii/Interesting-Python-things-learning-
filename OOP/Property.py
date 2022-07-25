
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    old = property(get_age, set_age)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
    
    @name.deleter
    def name(self):
        del self.__name


p = Person('Vitalii', 30)
p.old = 31
p.name = 'Vital'
print(p.old, p.name)
