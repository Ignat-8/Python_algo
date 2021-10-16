# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

col = 5
row = 4
# формируем матрицу размером col*row из случайных чисел
mas_numb = []
for j in range(0, row):
    mas_row = []
    for i in range(0, col):
        mas_row.append(random.randint(1, 100))
    mas_numb.append(mas_row)

print('Исходная матрица: ')
for i in range(0, row):
    print(*mas_numb[i])

# ищем строку минимальных значений
min_el = [el for el in mas_numb[0]]
for j in range(0, row):
    for i in range(0, col):
        if min_el[i] > mas_numb[j][i]:
            min_el[i] = mas_numb[j][i]

# ищем максимальное значение
max_el = min_el[0]
for el in min_el:
    if el > max_el:
        max_el = el

print('Минимальные значения ', min_el)
print('Максимальное значение ', max_el)
