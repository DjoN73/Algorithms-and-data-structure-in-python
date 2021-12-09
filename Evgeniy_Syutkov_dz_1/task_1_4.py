from random import randint, uniform, choice

print(randint(int(input('Введите число начала: ')), int(input('Введите число конца: '))))
print(uniform(int(input('Введите число начала: ')), int(input('Введите число конца: '))))
print(choice([chr(i) for i in range(ord(input('Символ начала: ')), ord(input('Символ конца: ')))]))
