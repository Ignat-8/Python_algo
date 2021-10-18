# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный
# случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random


def sort_merge(lst, start=0, end=None):
    """Сортировка методом слияния или деления исходного массива на части"""
    def subpart(lst, start, end, pivot_index):
        lst[start], lst[pivot_index] = lst[pivot_index], lst[start]
        pivot = lst[start]
        x = start + 1
        y = start + 1

        while y <= end:
            if lst[y] <= pivot:
                lst[y], lst[x] = lst[x], lst[y]
                x += 1
            y += 1

        lst[start], lst[x - 1] = lst[x - 1], lst[start]
        return x - 1

    if end is None:
        end = len(lst) - 1
    if end - start < 1:
        return

    pivot_index = random.randint(start, end)
    x = subpart(lst, start, end, pivot_index)
    sort_merge(lst, start, x - 1)
    sort_merge(lst, x + 1, end)
    return lst


mas = [random.randint(0, 49) for _ in range(0, 25)]
print('Исходный массив случайных чисел:\n', mas)
print('\nОтсортированный массив случайных чисел:\n', sort_merge(mas))
