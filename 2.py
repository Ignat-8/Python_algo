# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется
# как массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F.
# Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера:
# [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

HEX_DEC = {'0': 0, '1': 1, '2': 2, '3': 3,
           '4': 4, '5': 5, '6': 6, '7': 7,
           '8': 8, '9': 9, 'A': 10, 'a': 10,
           'B': 11, 'b': 11, 'C': 12, 'c': 12,
           'D': 13, 'd': 13, 'E': 14, 'e': 14,
           'F': 15, 'f': 15}

DEC_HEX = {0: '0', 1: '1', 2: '2', 3: '3',
           4: '4', 5: '5', 6: '6', 7: '7',
           8: '8', 9: '9', 10: 'A', 11: 'B',
           12: 'C', 13: 'D', 14: 'E', 15: 'F'}


def num_to_hex(n):
    """Преобразование десятичного числа в 16-ричное"""
    h = []
    while n > 0:
        d = 16
        while n/d > 16:
            d *= 16
        h.append(DEC_HEX[n//d])
        n = n - d * (n//d)
        if n < 16:
            h.append(DEC_HEX[n])
            n = 0
    return h


class hex_number:
    def __init__(self, h):
        self.h = h

    def __add__(self, obj):
        d1 = 0
        d2 = 0
        for i, el in enumerate(self.h[::-1]):
            d1 += HEX_DEC[el] * (16 ** i)
        for i, el in enumerate(obj.h[::-1]):
            d2 += HEX_DEC[el] * (16 ** i)
        return num_to_hex(d1 + d2)

    def __mul__(self, obj):
        d1 = 0
        d2 = 0
        for i, el in enumerate(self.h[::-1]):
            d1 += HEX_DEC[el] * (16 ** i)
        for i, el in enumerate(obj.h[::-1]):
            d2 += HEX_DEC[el] * (16 ** i)
        return num_to_hex(d1 * d2)


h1 = list(input('Введите первое 16-ричное число: '))
h2 = list(input('Введите второе 16-ричное число: '))
a = hex_number(h1)
b = hex_number(h2)
print(f'Сумма чисел {h1} + {h2} = {a + b}')
print(f'Произведение чисел {h1} * {h2} = {a * b}')
