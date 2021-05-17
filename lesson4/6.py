# task_6 (скрипт)
from itertools import cycle, count
list_num = []
for i in count(int(input('Введите число, с которого начать генерацию чисел: '))):
    if i > 19:
        break
    else:
        list_num.append(i)
print(f'Список сгенерированных числе функцией count: {list_num}')

my_list = ['CD', 125, 9, True]
fin_list = []
k = 0
for el in cycle(my_list):
    if k > 16:
        break
    else:
        fin_list.append(el)
    k += 1
print(f'Список повторенных элементов списка функцией cycle: {fin_list}')