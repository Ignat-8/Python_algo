# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

mas_number = [random.randint(-100, -1) for i in range(10)]
print(f'Исходный массив случайных чисел: {mas_number}')

max_poz = 0
max_numb = mas_number[max_poz]
for i, el in enumerate(mas_number):
    if el > max_numb:
        max_poz = i
        max_numb = el

print(f'Максимальное число {max_numb} находитя в позиции {max_poz+1}')
