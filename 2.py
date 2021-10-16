# Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена» и используя алгоритм «Решето Эратосфена»

import time


def time_func(func):
    def wrapper(x):
        start_time = time.time()
        res = func(x)
        end_time = time.time()
        print('Время исполнения', end_time-start_time)
        return res
    return wrapper


def prime(n):
    if n == 1:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


@time_func
def prime_count_denominator(n_i):
    # Сложность этого алгоритма O(n*(n^0.5))
    # при вычислении 100-тысячного простого числа затрачивается 15.7 секунды
    p_i = 0  # счетчик простых чисел
    i = 1
    while p_i != n_i:
        i += 1
        if prime(i) is True:
            p_i += 1
    return i


@time_func
def prime_eratosfen(n_i):
    # сложность этого алгоритма O(n*log(log(n)))
    # при вычислении 100-тысячного простого числа затрачивается 0.8 секунды
    n = 20 * n_i  # в диапазоне [1, n] количество простых чисел примерно равно n/Ln(n)
    numb = list(range(n))
    numb[0] = numb[1] = False
    p_i = 0  # счетчик простых чисел
    for i in range(2, n):
        if numb[i]:
            for j in range(2 * i, n, i):
                numb[j] = False
            p_i += 1
            if p_i == n_i:
                return i


p_i = int(input('Введите порядковый номер простого числа: '))
print(f'Метод перебора делителей:')
print(f'{p_i}-ое простое число = {prime_count_denominator(p_i)}')

print(f'\nМетод решета Эратосфена:')
print(f'{p_i}-ое простое число = {prime_eratosfen(p_i)}')
