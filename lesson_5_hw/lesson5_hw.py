# task_1
first_file = open('file_1.txt', 'w')
bl = True
while bl:
    line = input('Введите данные в файл')
    if line == '':
        bl = False
    else:
        first_file.writelines(line+'\n')
first_file.close()
first_file = open('file_1.txt', 'r')
info = first_file.readlines()
print(info)
first_file.close()

# task_2
second_file = open('file_2.txt', 'r')
count_str = 0
for line in second_file:
    count_str += 1
    bl = False
    count_words = 0
    for word in line:
        if word != ' ' and bl == False:
            count_words += 1
            bl = True
        elif word == ' ':
            bl = False
    print(f'Количество слов в {count_str}-ой строке: {count_words}')
print(f'Количество строк в файле: {count_str}')
second_file.close()

# task_3
with open('file_3.txt', 'r', encoding = 'utf-8') as third_file:
    fio_list = []
    av_salary = 0
    sum_sal = 0
    line_count = 0
    for line in third_file:
        line_count += 1
        fio, sal = line.split()
        if int(sal) < 20000:
            fio_list.append(fio)
        sum_sal += int(sal)
    av_salary = sum_sal / line_count
    print(f'Средняя зароботная плата={av_salary:.2f}')
    for i in fio_list:
        print(f'Заработная плата меньше 20 тыс у {i}')

#task_4
rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
result_list = []
with open('file_4.txt', 'r', encoding = 'utf-8') as fourth_file:
    for line in fourth_file:
        line = line.split(' ', 1)
        result = open('file_4_result.txt', 'a')
        result.writelines(rus[line[0]] + ' ' + line[1])
result.close()

# task_5
sum = 0
try:
    with open('file_5.txt', 'w+') as fifth_file:
        line = input('Введите числа через пробел:')
        fifth_file.writelines(line)
        numbers = line.split()
    for number in numbers:
        sum += int(number)
    print(f'Сумма чисел равна: {sum}')
except ValueError:
    print('Введены не только числа!!!Ошибка')

# task_6
with open('file_6.txt', 'r') as sixth_file:
    subjects = {}
    for line in sixth_file.readlines():
        data = line.replace('(', ' ').split()
        sum = 0
        for i in data:
            if i.isdigit():
                sum += int(i)
        subjects[data[0][:-1]] = sum
    print(subjects)



# task_7
import json
result_profit = 0
i = 0
info_firm = {}
av_profit = {}
prof_av = 0
itog_list = []
with open('file_7.txt', 'r') as f:
    for line in f:
        firm, type_firm, earning, damage = line.split()
        profit = int(earning) - int(damage)
        info_firm[firm] = profit
        if profit >= 0:
            result_profit += profit
            i += 1
    if i != 0:
        prof_av = result_profit / i
        av_profit['av_profit'] = round(prof_av, 2)
    else:
        print('Прибыль отсутствует у всех компаний!')
    itog_list = [info_firm, av_profit]
    print(itog_list)
with open('file_7.json', 'w') as f:
    json.dump(itog_list, f)

