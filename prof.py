"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма
"""

import cProfile
from timeit import default_timer, repeat

num = 20 ** 700


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        nums = enter_num % 10
        revers_num = (revers_num + nums / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        nums = enter_num % 10
        revers_num = (revers_num + nums / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


setup = """
from __main__ import revers,num
    """

st = "revers(num)"

setup_2 = """
from __main__ import revers_2,num
    """

st_2 = "revers_2(num)"

setup_3 = """
from __main__ import revers_3,num
    """

st_3 = "revers_3(num)"

print(f'{min(repeat(st, setup, default_timer, 3, 1))}')
cProfile.run('revers(num, revers_num=0)')

print(f'{min(repeat(st_2, setup_2, default_timer, 3, 1))}')
cProfile.run('revers_2(num, revers_num=0)')

print(f'{min(repeat(st_3, setup_3, default_timer, 3, 1))}')
cProfile.run('revers_3(num)')
