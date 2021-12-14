
n = int(input('Введите число: '))
a = 0
for i in range(1, n + 1):
    a += i
b = n * (n + 1) / 2
if a == b:
    print(f'Для n = {n} - True')
else:
    print(f'Для n = {n} - False')
