from random import randint

my_list = [randint(-50, 50) for _ in range(50)]
print(my_list)

min_idx = 0

for i in my_list:
    if my_list[min_idx] > i:
        min_idx = my_list.index(i)

if my_list[min_idx] >= 0:
    print('В массиве нет отрицательных элементов')
else:
    print(f'Минимальный отрицательный элемент: {my_list[min_idx]} под индексом {min_idx}')
