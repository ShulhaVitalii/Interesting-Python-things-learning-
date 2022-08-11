import time


def check_time(func):
    def wrapper(*args, **kwargs):
        st = time.time()
        r = func(*args, **kwargs)
        et = time.time()
        dt = et - st
        print(f'Function work time : {dt}')
        return r
    return wrapper


@check_time
def get_nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


@check_time
def get_fast_nod(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a


res = get_nod(2, 1000000)
res1 = get_fast_nod(652623, 107876464)
print(res1)


### Class decorator


class Router:
    app = {}

    @classmethod
    def get(cls, path):
        return cls.app.get(path)

    @classmethod
    def add_callback(cls, path, func):
        cls.app[path] = func


class Callback:
    def __init__(self, path, router_cls):
        self.path = path
        self.router_cls = router_cls

    def __call__(self, func):
        self.router_cls.add_callback(self.path, func)


@Callback('/about', Router)
def about():
    return '<h1>About</h1>'


route = Router.get('/about')
ret = route()
assert ret == '<h1>About</h1>', "декорированная функция вернула неверные данные"

route = Router.get('/')
assert route is None, "Класс Router, при вызове метода get, вернул неверные данные"
