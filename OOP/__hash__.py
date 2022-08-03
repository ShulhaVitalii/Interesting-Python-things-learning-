class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(1, 20)

print(hash(p1), hash(p2), sep='\n')

d = {}
d[p1] = 1
d[p2] = 2
d[p3] = 3
print(d)


##########


class ShopItem:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __hash__(self):
        return hash((self.name.lower(), self.price, self.weight))

    def __eq__(self, other):
        return hash(self) == hash(other)


lst_in = ['Системный блок: 1500 75890.56', 'Монитор Samsung: 2000 34000', 'Клавиатура: 200.44 545',
          'Монитор Samsung: 2000 34000']
# shop_items = {}
#
# for i in lst_in:
#     item = ShopItem(*(i.split(':')[0], i.split()[-2], i.split()[-1]))
#     if hash(item) not in [hash(i) for i in shop_items]:
#         shop_items[item] = [item, 1]
#     else:
#         shop_items[item][1] += 1
lst = [ShopItem(i.split(":")[0], *i.split(":")[1].strip().split(' ')) for i in lst_in]
shop_items = {i: [i, lst.count(i)] for i in lst}

print(shop_items)


it1 = ShopItem('name', 10, 11)
it2 = ShopItem('name', 10, 11)
assert hash(it1) == hash(it2), "разные хеши у равных объектов"

it2 = ShopItem('name', 10, 12)
assert hash(it1) != hash(it2), "равные хеши у разных объектов"

it2 = ShopItem('name', 11, 11)
assert hash(it1) != hash(it2), "равные хеши у разных объектов"

it2 = ShopItem('NAME', 10, 11)
assert hash(it1) == hash(it2), "разные хеши у равных объектов"

name = lst_in[0].split(':')
for sp in shop_items.values():
    assert isinstance(sp[0], ShopItem) and type(sp[1]) == int, "в значениях словаря shop_items первый элемент должен быть объектом класса ShopItem, а второй - целым числом"

v = list(shop_items.values())
if v[0][0].name.strip() == "Системный блок":
    assert v[0][1] == 1 and v[1][1] == 2 and v[2][1] == 1 and len(v) == 3, "неверные значения в словаре shop_items"

if v[0][0].name.strip() == "X-box":
    assert v[0][1] == 2 and v[1][1] == 1 and v[2][1] == 2 and len(v) == 3, "неверные значения в словаре shop_items"
    
 

######


class DataBase:
    def __init__(self, path: str):
        self.path = path
        self.dict_db = {}

    def write(self, record):
        print(record.fio)
        if hash(record) not in [hash(i) for i in self.dict_db]:
            self.dict_db[record] = [record]
        else:
            for i in [i for i in self.dict_db]:
                if hash(i) == hash(record):
                    self.dict_db[i].append(record)

    def read(self, pk):
        for r in self.dict_db:
            if r.pk == pk:
                return r


class Record:
    num = (i for i in range(1, 1000000))

    def __init__(self, fio: str, descr: str, old: int):
        self.pk = next(self.num)
        self.fio = fio
        self.descr = descr
        self.old = old

    def __hash__(self):
        return hash((self.fio.lower(), int(self.old)))

    def __eq__(self, other):
        return hash(self) == hash(other)




db = DataBase('Path')
lst_in = ['Балакирев С.М.; программист; 33',
'Кузнецов А.В.; разведчик-нелегал; 35',
'Суворов А.В.; полководец; 42',
'Иванов И.И.; фигурант всех подобных списков; 26',
'Балакирев С.М.; преподаватель; 33']
for i in lst_in:
    i = i.split(';')
    record = Record(i[0].strip(), i[1].strip(), int(i[2].strip()))
    db.write(record)
    print('record hash : ', hash(record))


db22345 = DataBase('123')
r1 = Record('fio', 'descr', 10)
r2 = Record('fio', 'descr', 10)
assert r1.pk != r2.pk, "равные значения атрибута pk у разных объектов класса Record"

db22345.write(r2)
r22 = db22345.read(r2.pk)
assert r22.pk == r2.pk and r22.fio == r2.fio and r22.descr == r2.descr and r22.old == r2.old, "при операциях write и read прочитанный объект имеет неверные значения атрибутов"

assert len(db22345.dict_db) == 1, "неверное число объектов в словаре dict_db"

fio = lst_in[0].split(';')[0].strip()
v = list(db.dict_db.values())
if fio == "Балакирев С.М.":
    assert len(v[0]) == 2 and len(v[1]) == 1 and len(v[2]) == 1 and len(
        v[3]) == 1, "неверно сформирован словарь dict_db"

if fio == "Гейтс Б.":
    assert len(v[0]) == 2 and len(v[1]) == 2 and len(v[2]) == 1 and len(
        v[3]) == 1, "неверно сформирован словарь dict_db"


   
