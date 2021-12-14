res = 0

while True:
    sign = input('Введите знак операции: ')
    if sign == '0':
        print('Выход из программы')
        break
    if sign in ('+', '-', '*', '/'):
        a = int(input('Введите первое число: '))
        b = int(input('Введите второе число: '))
        if sign == '+':
            res = a + b
            print(f'{a} {sign} {b} = {res}')
        elif sign == '-':
            res = a - b
            print(f'{a} {sign} {b} = {res}')
        elif sign == '*':
            res = a * b
            print(f'{a} {sign} {b} = {res}')
        elif sign == '/':
            if b != 0:
                res = a / b
                print(f'{a} {sign} {b} = {res}')
            else:
                print('На ноль делить нельзя!')
    else:
        print('Неверный знак операцции')
        sign = input('Введите знак операции')
