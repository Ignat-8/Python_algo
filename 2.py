# Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака. Объяснить полученный результат.

def operation_and(h1, h2):
    h = []
    h1 = h1[::-1]
    h2 = h2[::-1]
    for i in range(len(h1)):
        if int(h1[i]) and int(h2[i]):
            h.append('1')
        else:
            h.append('0')
    return ''.join(h[::-1])


def operation_or(h1, h2):
    h = []
    h1 = h1[::-1]
    h2 = h2[::-1]
    for i in range(len(h1)):
        if int(h1[i]) or int(h2[i]):
            h.append('1')
        else:
            h.append('0')
    return ''.join(h[::-1])


def operation_xor(h1, h2):
    h = []
    for i in range(len(h1)):
        if int(h1[i]) or int(h2[i]):
            h.append('0')
        else:
            h.append('1')
    return ''.join(h[::-1])


def shift_right(h):
    h = list(h[::-1])
    for i in range(len(h)-1):
        h[i] = h[i + 1]
    h[len(h)-1] = '0'
    return ''.join(h[::-1])


def shift_left(h):
    h = list(h)
    h.append('0')
    return ''.join(h)


d1 = 5
d2 = 6
h1 = bin(d1).split('0b')[1]
print('число 5 - ', h1)

h2 = bin(d2).split('0b')[1]
print('число 6 - ', h2)

print('побитовая операция AND ', operation_and(h1, h2))
print('побитовая операция OR ', operation_or(h1, h2))
print('побитовая операция XOR ', operation_xor(h1, h2))
print('двойной сдвиг вправо ', shift_right(shift_right(h2)))  # двойное целочисленное деление на 2
print('двойной сдвиг влево ', shift_left(shift_left(h2)))  # двойное умножение на 2
