even = 0
odd = 0
number = input('Введите число: ')

for i in number:
    if int(i) % 2 == 0:
        even += 1
    else:
        odd += 1
print(f'У числа {number}: {even} четных чисел, {odd} нечетных чисел')
