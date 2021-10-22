# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

list_even = []
list_odd = []
d = int(input('Введите число >0: '))

while d > 1:
    if (d % 10) % 2 == 0 and int(d % 10) not in list_even:
        list_even.append(int(d % 10))
    if (d % 10) % 2 > 0 and int(d % 10) not in list_odd:
        list_odd.append(int(d % 10))
    d = (d-d % 10)/10

print(f'Список четных цифр числа {list_even}')
print(f'Список не четных цифр числа {list_odd}')
