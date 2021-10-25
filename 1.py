# Определить количество различных подстрок с использованием хеш-функции. Задача: на вход функции
# дана строка, требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком

import hashlib
import random

s = ''.join([chr(random.randint(97, 122)) for _ in range(40)])
print('Исходная строка:', s)

cnt_dif = 0  # количество различных подстрок
cnt_total = 0  # общее число подстрок

for i in range(2, len(s)):  # перебираем возможные длины подстрок
    for j in range(len(s) - i + 1):  # перебираем все возможные подстроки
        cnt = 0  # счетчик числа совпадений подстрок
        h_subs = hashlib.sha1(s[j:j+i].encode('utf-8')).hexdigest()
        for t in range(len(s) - i + 1):  # ищем совпадение подстрок
            if h_subs == hashlib.sha1(s[t:t+i].encode('utf-8')).hexdigest():
                cnt += 1
        if cnt == 1:  # такая подстрока найдена один раз
            cnt_dif += 1
        if cnt > 1:  # такая подстрока найдена более одного раза
            print('НЕ уникальная подстрока:', s[j:j+i])
        cnt_total += 1

print('cnt_total=', cnt_total, ', cnt_dif=', cnt_dif)
