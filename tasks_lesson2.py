# task_1
my_list = [23, 'wave', 25.48, True, ['str', False], ('f', 25)]
for el in my_list:
    print(type(el))

# task_2
my_list_2 = list(input('Введите элементы списка - '))
print(my_list_2)
n = len(my_list_2)
i = 0
while i < n - 1:
    b = my_list_2.pop(i+1)
    my_list_2.insert(i, b)
    i = i + 2
print(my_list_2)

# task_3
month = int(input('Введите месяц (от 1 до 12) - '))
seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']
seasons_dict = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}
if month == 12 or 0 < month < 3:
    print(seasons_list[0], seasons_dict.get(1))
elif 2 < month < 6:
    print(seasons_list[1], seasons_dict.get(2))
elif 5 < month < 9:
    print(seasons_list[2], seasons_dict.get(3))
elif 8 < month < 12:
    print(seasons_list[3], seasons_dict.get(4))
else:
    print('Такого месяца нет, введите число от 1 до 12!')

# task_4
input_str = input('Введите строку из нескольких слов - ')
result_list = input_str.split(' ')
print(result_list)
num = 0
for el in result_list:
    num = num + 1
    print(f"{num} {el[:10]}")

# task_5
score = [9, 7, 6, 2, 1]
new_el = int(input('Введите натуральное число, Для завершение програмы введите 99 - '))
while new_el != 99:
    for el in range(len(score)):
        if new_el <= score[-1]:
            score.append(new_el)
            break
        elif score[el+1] < new_el <= score[el]:
            score.insert(el+1, new_el)
            break
        elif new_el > score[0]:
            score.insert(0, new_el)
    print(f"Текущий рейтинг:{score}")
    new_el = int(input('Введите натуральное число - , Для завершение програмы введите 99 - '))

# task_6
list_products = []
list_cost = []
list_names = []
list_count = []
list_unit = []
n_product = int(input('Введите количество вводимых товаров- '))
n = 1
while n <= n_product:
    name = input('Введите название товара- ')
    cost = int(input('Введите цену товара- '))
    count = int(input('Введите количество товара- '))
    unit_measure = input('Введите единицу измерения товара- ')
    dict_product = {'Название': name, 'Цена': cost, 'Количество': count, 'Единица измерения': unit_measure}
    tuple_product = (n, dict_product)
    list_products.append(tuple_product)
    list_names.append(dict_product.get('Название'))
    list_cost.append(dict_product.get('Цена'))
    list_count.append(dict_product.get('Количество'))
    list_unit.append(dict_product.get('Единица измерения'))
    n = n + 1

for i in list_products:
    print(i)
analytics_result = {'Название': list_names, 'Цена': list_cost,
                    'Количество': list_count, 'Единица измерения': list_unit}
for key, value in analytics_result.items():
    print(key, value)
