# Определить, какое число в массиве встречается чаще всего.

def count_numb_in_mas(src):
    """Формирует словарь чисел с подсчетом их повторений в заданном списке src"""
    return_dict = {}
    for num in src:
        return_dict.setdefault(num, 0)
        return_dict[num] += 1
    return return_dict


mas_numb = input('Введите массив чисел через запятую: ').split(',')
cnt_numb = count_numb_in_mas(mas_numb)
max_cnt = 0
max_key = ''
for key in cnt_numb:
    if cnt_numb[key] > max_cnt:
        max_cnt = cnt_numb[key]
        max_key = key

print(f'Число {max_key} встречается {max_cnt} раз')
