# mixins
# multi inheritance
# MRO - Method Resolution Order


class Goods:
    def __init__(self, name, weight, price):
        super().__init__()   # for call init in MixinLog
        print('Init Goods')
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f'{self.name}, {self.weight}, {self.price}')


class MixinLog:
    ID = 0

    def __init__(self):
        print('Init MixinLog')
        self.ID += 1
        self.id = self.ID

    def save_sell_log(self):
        print(f'{self.id}: sell in 00:00')

    def print_info(self):
        print(f'print_info from MixinLog')


class NoteBook(Goods, MixinLog):
    pass


n = NoteBook('Acer', 1.5, 30000)
n.print_info()
n.save_sell_log()

print(NoteBook.__mro__)

MixinLog.print_info(n)
