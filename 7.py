# По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
# составленного из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним,
# равнобедренным или равносторонним.

d1 = int(input('Введите длину первого отрезка: '))
d2 = int(input('Введите длину второго отрезка: '))
d3 = int(input('Введите длину третьего отрезка: '))

if d1 + d2 > d3 and d1 + d3 > d2 and d2 + d3 > d1:
    if d1 == d2 == d3:
        print('это равносторонний треугольник')
    elif d1 == d2 or d1 == d3 or d2 == d3:
        print('это равнобедренный треугольник')
    else:
        print('это разносторонний треугольник')
else:
    print('такого треугольника не существует')
