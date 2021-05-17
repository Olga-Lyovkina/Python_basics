# task_5
from functools import reduce

array = [el for el in range(100, 1001) if el % 2 == 0]
result = reduce(lambda x, y: x * y, array)
print(f'Результат произведения чисел: {result}')