# http://python-3.ru/page/multiprocessing

import os
from multiprocessing import Process, current_process


def doubler(number):
    """
    Функция умножитель на два
    """
    result = number * 2
    proc_name = current_process().name
    print('{0} doubled to {1} by process id: {2}'.format(
        number, result, proc_name))


if __name__ == '__main__':
    numbers = [5, 10, 15, 20, 25]
    procs = []
    proc = Process(target=doubler, args=(5,))

    for index, number in enumerate(numbers):
        proc = Process(target=doubler, args=(number,))
        procs.append(proc)
        proc.start()

    proc = Process(target=doubler, name='Test', args=(2,))
    proc.start()
    procs.append(proc)

    for proc in procs:
        proc.join()
        
