k = int(input('Введите количество элементов последовательности: '))
num = 1
i = 0
sum = 0
while i < k:
    sum += num
    num /= -2
    i += 1
print(f'Сумма чисел = {sum}')
