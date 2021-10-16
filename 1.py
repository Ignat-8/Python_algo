# Проанализировать скорость и сложность одного любого алгоритма,
# разработанных в рамках домашнего задания первых трех уроков.

# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random
import time


def time_func(func):
    def wrapper():
        start_time = time.time()
        res = func()
        end_time = time.time()
        print('Время исполнения', end_time-start_time)
        return res
    return wrapper


@time_func
def main():
    # формируем список из 20 случайных чисел от 1 до 100
    mas_number = [random.randint(1, 100) for i in range(100000)]
    print(f'Исходный массив чисел:\n{mas_number}')
    # допустим в первой позиции находится минимальный и максимальный элементы
    max_poz = 0
    min_poz = 0
    max_numb = mas_number[max_poz]
    min_numb = mas_number[min_poz]
    # сравниваем первый элемент со всем списком
    for i, el in enumerate(mas_number):
        if el > max_numb:
            max_numb = el
            max_poz = i
        if el < min_numb:
            min_numb = el
            min_poz = i

    print('min_poz = ', min_poz, ', min = ', min_numb)
    print('max_poz = ', max_poz, ', max = ', max_numb)
    # ищем сумму чисел между минимальным и максимальным элементом
    sum_numb = 0
    if max_poz > min_poz:
        for i in range(min_poz+1, max_poz):
            sum_numb += mas_number[i]

    if max_poz < min_poz:
        for i in range(max_poz+1, min_poz):
            sum_numb += mas_number[i]
    return sum_numb


print(f'Сумма чисел между минимальным и максимальным равна {main()}')
# Сложность алгоритма равна O(n),т.е. линейный, т.к. сложность поиска минимума и максимума равна n
# и в худшем случае для поиска суммы нужно еще раз пройти по списку длиной n, т.е. получаем 2*n
# Время выполнения при длине списка 1000 в диапазоне 0.001-0.003 сек
# Время выполнения при длине списка 10 000 в диапазоне 0.02-0.045 сек
# Время выполнения при длине списка 100 000 в диапазоне 0.1-0.2 сек
