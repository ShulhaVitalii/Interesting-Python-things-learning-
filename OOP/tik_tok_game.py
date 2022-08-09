import random


class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

    def __init__(self):
        self.pole = [[Cell() for _ in range(3)]for _ in range(3)]

    def init(self):
        self.pole = [[Cell() for _ in range(3)]for _ in range(3)]

    def show(self):
        for i in range(3):
            for j in range(3):
                print(self.pole[i][j].value, end=' ')
            print()
        print()

    def human_go(self):
        i, j = input('Entered coords : ').split()
        self.__setitem__((int(i), int(j)), self.HUMAN_X)

    def computer_go(self):
        while True:
            i = random.randint(0, 2)
            j = random.randint(0, 2)
            if self.pole[i][j].is_free:
                self.__setitem__((int(i), int(j)), self.COMPUTER_O)
                return

    @property
    def is_human_win(self):
        flag = False
        if self.pole[0][2].value == self.pole[1][1].value == self.pole[2][0].value == self.HUMAN_X:
            return True
        for i in range(3):
            if self.pole[i][i].value == self.HUMAN_X:
                flag = True
            else:
                flag = False

            if self.pole[i][0].value == self.pole[i][1].value == self.pole[i][2].value == self.HUMAN_X:
                return True
            if self.pole[0][i].value == self.pole[1][i].value == self.pole[2][i].value == self.HUMAN_X:
                return True
        return flag

    @property
    def is_computer_win(self):
        flag = False
        if self.pole[0][2].value == self.pole[1][1].value == self.pole[2][0].value == self.COMPUTER_O:
            return True
        for i in range(3):
            if self.pole[i][i].value == self.COMPUTER_O:
                flag = True
            else:
                flag = False

            if self.pole[i][0].value == self.pole[i][1].value == self.pole[i][2].value == self.COMPUTER_O:
                return True
            if self.pole[0][i].value == self.pole[1][i].value == self.pole[2][i].value == self.COMPUTER_O:
                return True
        return flag

    @property
    def is_draw(self):
        if self.is_computer_win == self.is_human_win == self.have_free_cells == False:
            return True
        return False

    def have_free_cells(self):
        for i in range(3):
            for j in range(3):
                if self.pole[i][j].value == 0:
                    return True
        return False

    def __getitem__(self, item):
        if type(item[1]) == int and type(item[0]) == int:
            return self.pole[item[0]][item[1]].value

        if type(item[1]) == slice:
            res = self.pole[item[0]][item[1]]
            return tuple(i.value for i in res)

        if type(item[0]) == slice:
            pole = [[0 for _ in range(3)] for _ in range(3)]
            for i in range(3):
                for j in range(3):
                    pole[i][j] = self.pole[j][i]
            return tuple(i.value for i in pole[item[1]])

    def __setitem__(self, key, value):
        if 0 > key[0] >= 3 or -1 >= key[1] >= 3:
            raise IndexError('некорректно указанные индексы')

        if bool(self.pole[key[0]][key[1]]):
            self.pole[key[0]][key[1]].value = value
            self.pole[key[0]][key[1]].is_free = False
        else:
            raise ValueError('клетка уже занята')
        return self

    def __bool__(self):
        if not self.have_free_cells:
            return False
        if self.is_human_win:
            return False
        if self.is_computer_win:
            return False
        return True


class Cell:
    def __init__(self):
        self.is_free = True
        self.value = 0

    def __bool__(self):
        return True if self.value == 0 else False



cell = Cell()
assert cell.value == 0, "начальное значение атрибута value объекта класса Cell должно быть равно 0"
assert bool(cell), "функция bool для объекта класса Cell вернула неверное значение"
cell.value = 1
assert bool(cell) == False, "функция bool для объекта класса Cell вернула неверное значение"

assert hasattr(TicTacToe, 'show') and hasattr(TicTacToe, 'human_go') and hasattr(TicTacToe, 'computer_go'), "класс TicTacToe должен иметь методы show, human_go, computer_go"

game = TicTacToe()
assert bool(game), "функция bool вернула неверное значения для объекта класса TicTacToe"
assert game[0, 0] == 0 and game[2, 2] == 0, "неверные значения ячеек, взятые по индексам"
game[1, 1] = TicTacToe.HUMAN_X
assert game[1, 1] == TicTacToe.HUMAN_X, "неверно работает оператор присваивания нового значения в ячейку игрового поля"

game[0, 0] = TicTacToe.COMPUTER_O
assert game[0, 0] == TicTacToe.COMPUTER_O, "неверно работает оператор присваивания нового значения в ячейку игрового поля"

game.init()
assert game[0, 0] == TicTacToe.FREE_CELL and game[1, 1] == TicTacToe.FREE_CELL, "при инициализации игрового поля все клетки должны принимать значение из атрибута FREE_CELL"

try:
    game[3, 0] = 4
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

game.init()
assert game.is_human_win == False and game.is_computer_win == False and game.is_draw == False, "при инициализации игры атрибуты is_human_win, is_computer_win, is_draw должны быть равны False, возможно не пересчитывается статус игры при вызове метода init()"

game[0, 0] = TicTacToe.HUMAN_X
game[1, 1] = TicTacToe.HUMAN_X
game[2, 2] = TicTacToe.HUMAN_X
assert game.is_human_win and game.is_computer_win == False and game.is_draw == False, "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"

game.init()
game[0, 0] = TicTacToe.COMPUTER_O
game[1, 0] = TicTacToe.COMPUTER_O
game[2, 0] = TicTacToe.COMPUTER_O
assert game.is_human_win == False and game.is_computer_win and game.is_draw == False, "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"


game = TicTacToe()
game.init()
step_game = 0
while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1


game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")
