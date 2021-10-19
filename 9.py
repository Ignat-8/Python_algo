# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.


def sum_number(n):
    """ Функция поиска суммы цифр числа """
    s = 0
    i = -1
    while i < len(n)-1:
        i += 1
        s += int(n[i])
    return s


def main(*args):
    """ Функция поиска числа с максимальной суммой цифр """
    # первый элемент запоминаем как максимальный
    max_number = args[0]
    max_sum = sum_number(max_number)

    for el in args:
        if sum_number(el) > max_sum:
            max_number = el
            max_sum = sum_number(max_number)

    return [max_number, max_sum]


inp_number = input('Введите натуральные числа через запятую: ').split(',')
print(f'Число с максимальной суммой цифр {main(*inp_number)}')
