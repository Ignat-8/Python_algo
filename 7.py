# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

mas_number = [random.randint(1, 100) for i in range(20)]
print(f'Исходный массив чисел {mas_number}')

if mas_number[1] <= mas_number[0]:
    min1 = mas_number[0]  # наибольшее из двух наименьших
    min2 = mas_number[1]  # наименьшее из двух наименьших
else:
    min1 = mas_number[1]  # наибольшее из двух наименьших
    min2 = mas_number[0]  # наименьшее из двух наименьших

for i in range(2, len(mas_number)):
    if min2 < mas_number[i] < min1:
        min1 = mas_number[i]
    if mas_number[i] <= min2:
        min1 = min2
        min2 = mas_number[i]

print(f'Первое минимальное число {min1}')
print(f'Второе минимальное число {min2}')
