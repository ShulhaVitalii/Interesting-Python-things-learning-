"""
Магические методы __getitem__, __setitem__ и __delitem__
https://stepik.org/lesson/701993/step/1?unit=702094
"""
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):  # For obj[item]
        if 0<= item < len(self.marks):
            return self.marks[item]
        else:
            raise IndexError('Wrong index')

    def __setitem__(self, key, value):   # For obj[key] = value
        if not isinstance(key, int) or key < 0:
            raise TypeError('Wrong key')

        if key >= len(self.marks):
            off = key + 1 - len(self.marks)
            self.marks.extend([None] * off)
        self.marks[key] = value

    def __delitem__(self, key):   # For del odj[key]
        if not isinstance(key, int) or key < 0:
            raise TypeError('Wrong key')

        del self.marks[key]



s1 = Student('Vitalii', [5, 5, 3, 2, 5])
s1[2] = 4
print(s1[2])
del s1[2]
s1[10] = 5
print(s1.marks)

