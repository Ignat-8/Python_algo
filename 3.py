# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

mas_number = [random.randint(1, 100) for i in range(10)]
print(f'Исходный массив случайных чисел: {mas_number}')

min_number = mas_number[0]
max_number = mas_number[0]
min_poz = 0
max_poz = 0
i = -1

for el in mas_number:
    i += 1
    if el > max_number:
        max_number = el
        max_poz = i
    if el < min_number:
        min_number = el
        min_poz = i

mas_number[min_poz] = max_number
mas_number[max_poz] = min_number

print(f'Минимальное число {min_number}')
print(f'Максимальное число {max_number}')
print(f'Измененный массив случайных чисел: {mas_number}')
