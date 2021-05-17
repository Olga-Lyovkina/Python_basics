# task_1 (скрипт)
from sys import argv

first_par, time, salary, bonus = argv
try:
    print(f'Выработка в часах:{int(time)}')
    print(f'Ставка в час:{float(salary)}')
    print(f'Премия:{float(bonus)}')
    result = int(time) * float(salary) + float(bonus)
    print(f'Заработная плата сотрудника: {result}')
except ValueError:
    print('Ввели некорректные данные, не числового формата')
