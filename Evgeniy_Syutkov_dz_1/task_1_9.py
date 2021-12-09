a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
c = int(input('Enter third number: '))

if c > a > b or b > a > c:
    print(f'Среднее число a={a}')
elif c > b > a or a > b > c:
    print(f'Среднее число b={b}')
else:
    print(f'Среднее число c={c}')
