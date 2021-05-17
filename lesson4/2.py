# task_2
numbers_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
modified_list = [numbers_list[num] for num in range(1, len(numbers_list)) if numbers_list[num - 1] < numbers_list[num]]
print(f'Исходный список: {numbers_list}')
print(f'Измененный список: {modified_list}')
