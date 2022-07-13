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
