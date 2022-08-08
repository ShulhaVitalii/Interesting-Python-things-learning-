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
