# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива.

import random


def sort_bubble(mas_numb):
    """Сортировка улучшенным методом пузырька"""
    n_stop = len(mas_numb) - 1
    n_start = 0
    while n_start < n_stop:
        min_n = mas_numb[n_start]
        for i in range(n_start, n_stop):
            if mas_numb[i] > mas_numb[i + 1]:
                mas_numb[i], mas_numb[i + 1] = mas_numb[i + 1], mas_numb[i]
            if mas_numb[i] < min_n:
                min_n = mas_numb[i]
        if mas_numb[n_start] == min_n:  # если в стартовой позиции находится минимальный элемент
            n_start += 1  # то увеличиваем стартовую позицию на 1
        n_stop -= 1
    return mas_numb


def mas_median(mas_numb, m):
    for j in range(m):
        c = 0
        for i in range(2 * m + 1):
            if mas_numb[i] != -1:
                if c == 0:  # запоминаем стартовые значения для поиска минимума и максимума
                    min_n = mas_numb[i]
                    max_n = mas_numb[i]
                    min_poz = i
                    max_poz = i
                    c = 1
                if mas_numb[i] < min_n:
                    min_poz = i
                    min_n = mas_numb[i]
                if mas_numb[i] > max_n:
                    max_poz = i
                    max_n = mas_numb[i]
        mas_numb[max_poz] = -1  # "вычеркиваем" из массива максимальное
        mas_numb[min_poz] = -1  # и минимальное число
    for _ in range(2 * m + 1):
        if mas_numb[_] != -1:  # не вычеркнутое значение является медианой массива
            return mas_numb[_]


m = int(input('Введите размер m массива: '))
mas = [random.randint(0, 99) for _ in range(2 * m + 1)]
mas_copy = [el for el in mas]
print('\nИсходный массив случайных чисел:\n', mas)
print('\nМедиана массива: ', mas_median(mas, m))
print('\nОтсортированный массив случайных чисел:\n', sort_bubble(mas_copy))
