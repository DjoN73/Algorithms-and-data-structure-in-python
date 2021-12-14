user_range = input('Введите последовательность: ')
num = input('Введите цифру для поиска: ')
count = 0

for i in user_range:
    if i == num:
        count += 1
print(f'Цифра {num} встречается {count} раз')
