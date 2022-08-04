class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):   # Call if __bool__ not in class
        print('__len__')
        return self.x ** 2 + self.y ** 2

    def __bool__(self):   # Using for bool(obj)
        print('__bool__')
        return self.x == self.y


p = Point(10, 0)
print(bool(p))

if p:
    print('Object p is True because p.x == p.y')
else:
    print('Object p is False because p.x != p.y')
    
    
#####


class Player:
    def __init__(self, name: str, old: int, score: int):
        self.name = name
        self.old = old
        self.score = score

    def __bool__(self):
        return self.score > 0


lst_in = ['Балакирев; 34; 2048', 'Mediel; 27; 0', 'Влад; 18; 9012', 'Nina P; 33; 0']
players = [Player(i.split(';')[0], int(i.split(';')[1].strip()), int(i.split(';')[2].strip())) for i in lst_in]
players_filtered = list(filter(lambda x: bool(x), players))

###


class MailBox:
    def __init__(self):
        self.inbox_list = []

    def receive(self):
        lst_in = ['sc_lib@list.ru; От Балакирева; Успехов в IT!',
          'mail@list.ru; Выгодное предложение; Вам одобрен кредит.',
          'Python ООП; Балакирев С.М.; 2022',
          'mail123@list.ru; Розыгрыш; Вы выиграли 1 млн. руб. Переведите 30 тыс. руб., чтобы его получить.']
        for i in lst_in:
            mail_from = i.split(';')[0]
            title = i.split(';')[1].strip()
            content = i.split(';')[2].strip()
            self.inbox_list.append(MailItem(mail_from, title, content))

class MailItem:
    def __init__(self, mail_from, title, content):
        self.mail_from = mail_from
        self.title = title
        self.content = content
        self.is_read = False

    def set_read(self, fl_read):
        self.is_read = fl_read

    def __bool__(self):
        return self.is_read


mail = MailBox()
mail.receive()
mail.inbox_list[0].set_read(True)
mail.inbox_list[-1].set_read(True)
inbox_list_filtered = list(filter(lambda x: bool(x), mail.inbox_list))


####

