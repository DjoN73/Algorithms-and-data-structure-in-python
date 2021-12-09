num = input('Введите трехзначное число: ')
a = 0
b = 1
for letter in num:
    a += int(letter)
    b *= int(letter)
print(f'Сумма цифр числа {num}: {a}')
print(f'Произведение цифр числа {num}: {b}')
