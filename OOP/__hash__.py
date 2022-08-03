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
    
    
