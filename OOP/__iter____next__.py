"""
__iter__, __next__
https://stepik.org/lesson/701994/step/1?unit=702095
"""


class FRange:
    def __init__(self, start=0.0, stop=0.0, step=1.0):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        self.value = self.start - self.step
        return self

    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration


class FRange2D:
    def __init__(self, start=0.0, stop=0.0, step=1.0, rows=5):
        self.rows = rows
        self.fr = FRange(start, stop, step)

    def __iter__(self):
        self.value = 0
        return self

    def __next__(self):
        if self.value < self.rows:
            self.value += 1
            return iter(self.fr)
        else:
            raise StopIteration


# fr = FRange(0, 2, 0.5)
# print(next(fr))
# print(next(fr))
# print(next(fr))
# print(next(fr))

fr1 = FRange(0, 2, 0.5)
print('FRange')
for i in fr1:
    print(i)

fr = FRange2D(0, 2, 0.5, 4)
print()
print('FRange2D')
for row in fr:
    for x in row:
        print(x, end=' ')
    print()

    
    
 ###########


class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job

    def __getitem__(self, item):
        d = {0: self.fio, 1: self.job, 2: self.old, 3: self.salary, 4: self.year_job}
        if item in d:
            return d[item]
        else:
            raise IndexError('неверный индекс')

    def __setitem__(self, key, value):
        d = {0: 'fio', 1: 'job', 2: 'old', 3: 'salary', 4: 'year_job'}
        if key in d:
            self.__dict__[d[key]] = value
        else:
            raise IndexError('неверный индекс')
        return self

    def __iter__(self):
        self.counter = -1
        return self

    def __next__(self):
        d = {0: 'fio', 1: 'job', 2: 'old', 3: 'salary', 4: 'year_job'}

        if self.counter+1 < len(d):
            self.counter += 1
            return self.__dict__[d[self.counter]]
        else:
            raise StopIteration


pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
pers[0] = 'Балакирев С.М.'
print(pers[0])
for v in pers:
    print(v)
pers[5] = 123 # IndexError


########


class TriangleListIterator:
    def __init__(self, lst):
        self._lst = lst

    def __iter__(self):
        for i in range(len(self._lst)):
            for j in range(i+1):
                yield self._lst[i][j]


lst = [['x00'],
       ['x10', 'x11'],
       ['x20', 'x21', 'x22'],
       ['x30', 'x31', 'x32', 'x33']]
it = TriangleListIterator(lst)
for x in it:  # последовательный перебор всех элементов списка: x00, x10, x11, x20, ...
    print(x)
it_iter = iter(it)
x = next(it_iter)

#########


class IterColumn:
    def __init__(self, lst, column):
        self._lst = lst
        self._column = column

    def __iter__(self):
        for i in range(len(self._lst)):
            for j in range(len(self._lst[i])):
                if j == self._column:
                    yield self._lst[i][j]

lst = [['x00', 'x01', 'x02'],
       ['x10', 'x11', 'x12'],
       ['x20', 'x21', 'x22'],
       ['x30', 'x31', 'x32']]

it = IterColumn(lst, 1)
for x in it:  # последовательный перебор всех элементов столбца списка: x01, x11, ..., xM2
    print(x)
    
    
