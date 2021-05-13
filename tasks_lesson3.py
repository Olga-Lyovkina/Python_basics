# task_1
def division_two_digits(num1, num2):
    if num2 == 0:
        result = 'Ошибка! Нельзя делить на 0'
    else:
        result = num1 / num2
    return result


print(f'Результат деления:{division_two_digits(10, -5)}')


# task_2
def get_user_data(**kwargs):
    return kwargs


print(get_user_data(name='Ольга', fio='Лёвкина',
                    year=1998, city='Минск', email='olyalyova@gmail.com', phone=45654564))


# task_3
def get_sum_two_lagest_digits(num1, num2, num3):
    if num1 >= num3 and num2 >= num3:
        result = num1 + num2
    elif num1 >= num2 and num3 >= num2:
        result = num1 + num3
    else:
        result = num2 + num3
    return result


print(f'Результат сложения чисел: {get_sum_two_lagest_digits(8, 10, 7)}')

# task_4
def exponentiation_number_method_2(x, y):
    result = 1
    if y == -1:
        result = 1 / x
    else:
        for i in range(1, abs(y) + 1):
            result = result * (1 / x)
    return result


def exponentiation_number_method_1(x, y):
    result = (x ** y)
    return result


while True:
    num1 = float(input('Введите действительное положительное число для возведени в степень-'))
    num2 = int(input('Введите целое отрицательное число (степень)-'))
    if num1 < 0 or isinstance(num1, float) == False:
        print('Вы ввели некорректное число для возведения в степень! Введите действительное положительное число!')
    elif num2 >= 0 or isinstance(num2, int) == False:
        print('Вы ввели некорректное-степень! Введите целое отрицательное число!')
    else:
        print(f'Результат возведения в степень первым способом: {exponentiation_number_method_1(num1, num2)}')
        print(f'Результат возведения в степень вторым способом: {exponentiation_number_method_2(num1, num2)}')
        break

# task_5

def sum_digits(input_str):
    list_num = input_str.split(' ')
    result = 0
    for i in list_num:
        if i.isdigit():
            result += int(i)
        else:
            break
    return result


sum_result = 0
while True:
    str_num = input('Введите строку чисел, разделенных пробелами-')
    if str_num == '':
        print(f'Final summary = {sum_result}')
        break
    else:
        sum_result += sum_digits(str_num)


# task_6
def int_func(words):
    result = words.title()
    return result


text = input('Введите строку латинских букв в нижнем регистре')
if text.islower():
    print(f'Result: {text} -> {int_func(text)}')
else:
    print('Ошибка! Введите строку в нижнем регистре')
