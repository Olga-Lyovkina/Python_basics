# task_2
numbers_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
modified_list = [el for num, el in enumerate(numbers_list) if numbers_list[num - 1] < numbers_list[num]]
modified_list.pop(0)
print(f'Исходный список: {numbers_list}')
print(f'Измененный список: {modified_list}')
