class MaxPooling:
    def __init__(self, step=(2, 2), size=(2, 2)):
        self.step = step
        self.size = size

    @staticmethod
    def matrix_checker(matrix):
        for i in matrix:
            if sum([True for num in i if type(num) in (int, float)]) != len(matrix[0]):
                raise ValueError("Неверный формат для первого параметра matrix.")
        return matrix

    def get_res(self, matrix):
        res = [[0] * (len(matrix) // self.step[1]) for _ in range(len(matrix) // self.step[0])]
        k = 0
        for i in range(0, len(matrix), self.step[0]):
            g = 0
            for j in range(0, len(matrix), self.step[1]):
                m = max(matrix[i][j], matrix[i][j + 1], matrix[i + 1][j], matrix[i + 1][j + 1])
                res[k][g] = m
                g += 1
            k += 1
        return res

    def __call__(self, matrix, *args, **kwargs):
        self.matrix_checker(matrix)

        # if len(matrix) % self.step[0] == 0:
        #     return self.get_res(matrix)
        #
        # elif len(matrix) % self.step[0] != 0:
        #     del matrix[-1]
        #
        # elif len(matrix[0]) % self.step[1] != 0:
        #     for i in matrix:
        #         del i[-1]
        #
        # return self.get_res(matrix)

        rangeI = range(self.size[1], len(matrix) + 1, self.step[1])
        rangeJ = range(self.size[0], len(matrix[0]) + 1, self.step[0])

        return [[max(matrix[y][x]
                     for y in range(i - self.size[1], i)
                     for x in range(j - self.size[0], j)
                     ) for j in rangeJ]
                for i in rangeI]


mp = MaxPooling(step=(2, 2), size=(2, 2))
m1 = [[1, 10, 10], [5, 10, 0], [0, 1, 2]]
m2 = [[1, 10, 10, 12], [5, 10, 0, -5], [0, 1, 2, 300], [40, -100, 0, 54.5]]
res1 = mp(m1)
res2 = mp(m2)

assert res1 == [[10]], "неверный результат операции MaxPooling"
assert res2 == [[10, 12], [40, 300]], f"неверный результат операции MaxPooling"

mp = MaxPooling(step=(3, 3), size=(2, 2))
m3 = [[1, 12, 14, 12], [5, 10, 0, -5], [0, 1, 2, 300], [40, -100, 0, 54.5]]
res3 = mp(m3)

assert res3 == [[12]], "неверный результат операции при MaxPooling(step=(3, 3), size=(2,2))"

try:
    res = mp([[1, 2], [3, 4, 5]])
except ValueError:
    assert True
else:
    assert False, "некорректо отработала проверка (или она отсутствует) на не прямоугольную матрицу"

try:
    res = mp([[1, 2], [3, '4']])
except ValueError:
    assert True
else:
    assert False, "некорректо отработала проверка (или она отсутствует) на не числовые значения в матрице"
