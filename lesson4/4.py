# task_4
initial_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 23, 7, 4, 11]
end_list = [el for el in initial_list if initial_list.count(el) == 1]
print(f'Исходный список: {initial_list}')
print(f'Измененный список: {end_list}')