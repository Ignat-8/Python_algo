# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными
# числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).

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


mas = [random.randint(-100, 99) for _ in range(0, 25)]
print('Исходный массив случайных чисел:\n', mas)
print('\nОтсортированный массив случайных чисел:\n', sort_bubble(mas))
