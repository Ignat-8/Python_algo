# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

numb = list(range(100))
numb[0] = numb[1] = False
numb_count = 0

for d in range(2, 9):
    for i in range(2 * d, 100, d):
        if numb[i]:
            numb[i] = False
            numb_count += 1

print(numb)
print(numb_count)
