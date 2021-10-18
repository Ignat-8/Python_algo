# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
# в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее
# эффективным использованием памяти.
# Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
# Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и
# разрядность вашей ОС.

# Версия моего Python 3.9.5, разрядность ОС 64 bit
# Рассмотрим пространственную сложность на примере поиска i-го по счёту простого числа без использования
# «Решета Эратосфена» и используя его

import sys


def prime(n):
    if n == 1:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1  # хранение целого числа занимает 28 байт
    return True


def prime_count_denominator(n_i):
    # Сложность этого алгоритма O(n*(n^0.5))
    # при вычислении 100-тысячного простого числа затрачивается 15.7 секунды
    p_i = 0  # счетчик простых чисел требует 28 байт
    i = 1  # порядковый номер простого числа так же требует 28 байт
    while p_i != n_i:
        i += 1
        if prime(i) is True:  # для вычисления простого требуется 28 байт
            p_i += 1
    # Итого для этого алгоритма требуется 3*28 = 84 байта
    return i


def prime_eratosfen(n_i):
    # сложность этого алгоритма O(n*log(log(n)))
    # при вычислении 100-тысячного простого числа затрачивается 0.8 секунды
    n = 20 * n_i  # в диапазоне [1, n] количество простых чисел примерно равно n/Ln(n)
    # для числа n требуется 28 байт
    numb = list(range(n))
    # numb имеет динамический размер, вычисляется по формуле = 56 байт пустой список + 8 байт размер ссылки на число * n
    # для 100-тысячного простого числа размер равет 16 МБайт
    numb[0] = numb[1] = False
    p_i = 0  # счетчик простых чисел, требуется 28 байт
    for i in range(2, n):  # для счетчика i требуется 28 байт
        if numb[i]:
            for j in range(2 * i, n, i):  # для счетчика j требуется 28 байт
                numb[j] = False
            p_i += 1
            if p_i == n_i:
                return i
    # Итого обьем памяти чуть больше 16 МБайт


p_i = int(input('Введите порядковый номер простого числа: '))
print(f'Метод перебора делителей:')
print(f'{p_i}-ое простое число = {prime_count_denominator(p_i)}')

print(f'\nМетод решета Эратосфена:')
print(f'{p_i}-ое простое число = {prime_eratosfen(p_i)}')

# Вывод - для поиска 100-тысячного простого числа требуется:
# 1. методом простого перебора делителей - 15.7 секунд и 84 байта памяти
# 2. методом решета Эратосфена - 0.8 секунды и примерно 16 МБайт памяти
