# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего
# и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

company = {}  # Словарь компаний
n = int(input('Введите число предприятий: '))
profit_total = 0  # общая прибыль всех предприятий
for i in range(n):
    company_name = input(f'Ведите название {i+1}-го предприятия: ')
    profit = []  # список прибылей по кварталам
    for j in range(4):
        p = int(input(f'Введите прибыль за {j+1}-ый квартал: '))
        profit.append(p)
        profit_total += p
    profit.append(sum(profit[0:4])/4)  # в пятом элементе храним среднюю прибыль для каждого предприятия
    company[company_name] = profit

print('\nТаблица предприятий:')
print(f'Название 1кв 2кв 3кв 4кв среднее')
for key in company:
    print(key, *company[key])

avg_profit = profit_total/(4 * n)
print(f'\nСредняя прибыль {avg_profit}')

print('\nСписок компаний с прибылью больше среднего:')
for key in company:
    if company[key][4] > avg_profit:
        print(key)

print('\nСписок компаний с прибылью меньше среднего:')
for key in company:
    if company[key][4] < avg_profit:
        print(key)
