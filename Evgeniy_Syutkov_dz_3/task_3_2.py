from random import randint

my_list = [randint(0, 100) for _ in range(10)]
result = []
for i in range(len(my_list)):
    if my_list[i] % 2 == 0:
        result.append(i)
print(my_list)
print(f'Индексы четных элементов: {result}')
