# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

mas_number = [random.randint(1, 100) for i in range(20)]
print(f'Исходный массив чисел {mas_number}')

max_poz = 0
min_poz = 0
max_numb = mas_number[max_poz]
min_numb = mas_number[min_poz]

for i, el in enumerate(mas_number):
    if el > max_numb:
        max_numb = el
        max_poz = i
    if el < min_numb:
        min_numb = el
        min_poz = i

print('min_poz = ', min_poz, ', min = ', min_numb)
print('max_poz = ', max_poz, ', max = ', max_numb)

sum_numb = 0
if max_poz > min_poz:
    for i in range(min_poz+1, max_poz):
        sum_numb += mas_number[i]

if max_poz < min_poz:
    for i in range(max_poz+1, min_poz):
        sum_numb += mas_number[i]

print(f'Сумма чисел между минимальным {min_numb} и максимальным {max_numb} равна {sum_numb}')
