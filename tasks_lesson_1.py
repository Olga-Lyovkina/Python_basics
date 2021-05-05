# task_1
city = input('Введите город, в котором Вы проживаете - ')
age = input('Введите свой возраст - ')
print('Вы проживаете в городе ', city, ' , Вам ', age, ' лет')

# task_2
time = input('Введите время в секундах - ')
time = int(time)
hour = time // 3600
min = (time - hour * 3600) // 60
sec = (time - hour * 3600 - min * 60)
print(hour, ':', min, ':', sec)

# task_3
num = input('Введите число - ')
result = int(num + num + num) + int(num + num) + int(num)
print('Результат:', num, '+', num + num, '+', num + num + num, '=', result)


# task_4
n = input('Введите целое положительное число- ')
n = int(n)
a = 1
max_digit = 0
n_pre = 0
while (n // a) > 0:
    n_pre = n // a
    ost = n_pre % 10
    if ost > max_digit:
        max_digit = ost
    a = a * 10
print('Наибольшая цифра в числе', n, '=', max_digit)


# task_5
proceeds = input('Выручка фирмы- ')
expenses = input('Издержки фирмы - ')
proceeds = int(proceeds)
expenses = int(expenses)
if proceeds > expenses:
    print('Фирма в прибыли')
    benefit = (proceeds - expenses) / proceeds * 100
    print('Рентабельность: ', benefit, '%')
    n_staff = input('Укажите количество сотрудников фирмы - ')
    n_staff = int(n_staff)
    profit_1 = (proceeds - expenses) / n_staff
    print('Прибыль фирмы в расчете на одного сотрудника: ', profit_1)
else:
    print('Фирма в убытке')


# task_6
a = input('Введите количество километров, пробежал в первый день - ')
b = input('Введите граничное значение, которое спортмен должен пробежать в день - ')
a = int(a)
b = int(b)
day = 1
while a <= b:
    a = a * 1.1
    day = day + 1
print('На ', day, '-й день спортмен достиг результата  - не менее', b)
