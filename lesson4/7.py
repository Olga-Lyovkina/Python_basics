# task_7
from random import randint


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


def generator():
    for i in range(2, 14):
        yield i


for el in generator():
    print(f'{el}- сгенерированное число')
    for el_0 in range(1, el + 1):
        print(f'{el_0}!={fact(el_0)}')