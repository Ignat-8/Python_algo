# Закодировать любую строку по алгоритму Хаффмана

from collections import Counter


class Node:
    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value


def get_code(head, codes=dict(), code=''):
    """Формирует словарь кодов для каждого символа"""
    if head is None:
        return

    if isinstance(head.value, str):
        codes[head.value] = code
        return codes
    # -----------------------------------
    get_code(head.left, codes, code + '0')
    get_code(head.right, codes, code + '1')
    # -----------------------------------
    return codes


def get_tree(string_in):
    string_count = Counter(string_in)
    # -------------------------------------------------
    if len(string_count) <= 1:  # для пустой строки 0
        node = Node(None)

        if len(string_count) == 1:
            node.left = Node([key for key in string_count][0])
            node.right = Node(None)

        string_count = {node: 1}
    # -------------------------------------------------
    while len(string_count) != 1:
        node = Node(None)
        # сортируем гистограмму символов в обратном порядке
        # чтобы в начале списка были редкие символы
        spam = string_count.most_common()[::-1]
        # print(spam)
        # ---------------------------------
        if isinstance(spam[0][0], str):
            node.left = Node(spam[0][0])
            # print('left is str', spam[0][0])
        else:
            node.left = spam[0][0]
            # print('left', spam[0][0])
        # ---------------------------------
        if isinstance(spam[1][0], str):
            node.right = Node(spam[1][0])
            # print('right is str', spam[1][0])
        else:
            node.right = spam[1][0]
            # print('right', spam[1][0])
        # удаляем добавленные в дерево элементы
        del string_count[spam[0][0]]
        del string_count[spam[1][0]]
        # ---------------------------------
        string_count[node] = spam[0][1] + spam[1][1]
        # ---------------------------------
    return [key for key in string_count][0]


def coding(string_in, codes):
    string_out = ''
    # --------------------
    for el in string_in:
        string_out += codes[el]
        string_out += ' '
    # --------------------
    return string_out


def decoding(string_in, codes):
    string_in = string_in.split(' ')
    string_out = ''
    for el_code in string_in:
        for el in codes:
            if el_code == codes[el]:
                string_out += el
    return string_out


# функция для вычисления высоты дерева
def height(node):
    """Определяет высоту дерева"""
    if node is None:
        return 0
    else:
        left_height = height(node.left)
        right_height = height(node.right)

    if left_height > right_height:
        return left_height + 1
    else:
        return right_height + 1


# функция для распечатки элементов на определенном уровне дерева
def print_given_level(head, level, tp=''):
    if head is None:
        return
    if level == 1:
        if tp != '':
            print(f'{tp}:{head.value}', end=' ')
        else:
            print(f'head:{head.value}', end='')
    elif level > 1:
        print_given_level(head.left, level - 1, 'left')
        print_given_level(head.right, level - 1, 'right')
    return ''


# функция для распечатки дерева
def print_level_order(head):
    h = height(head)
    i = 1
    while i <= h:
        print_given_level(head, i)
        print()
        i += 1
    return ''


string = input('Введите строку для кодирования :')
tree = get_tree(string)  # формируем дерево символов
print('дерево символов:')
print(print_level_order(tree))

codes = get_code(tree)  # формируем код для каждого символа
print('словарь кодов:', codes)

coding_str = coding(string, codes)  # кодируем строку
print('закодированная строка:', coding_str)

decoding_str = decoding(coding_str, codes)  # декодируем строку
print('декодированная строка:', decoding_str)
