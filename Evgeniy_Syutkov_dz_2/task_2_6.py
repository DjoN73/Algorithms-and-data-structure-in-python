from random import randint

num = randint(0, 100)

i = 1
while i <= 10:
    answer = int(input('Введите число: '))
    if answer == num:
        print('Вы угадали!')
        break
    else:
        if answer > num:
            print('Неверно! Загаданное число меньше.')
        else:
            print('Неверно! Загаданное число больше.')
    i += 1
if i > 10:
    print(f'Вы проиграли. Загаданное число: {num}')
