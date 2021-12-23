from random import randint

rand_list = [randint(0, 99) for _ in range(10)]
print(f'Массив до изменения: {rand_list}')

max_num = rand_list[0]
min_num = rand_list[0]

for i in rand_list:
    if i > max_num:
        max_num = i
    elif i < min_num:
        min_num = i
idx_max = rand_list.index(max_num)
idx_min = rand_list.index(min_num)
rand_list[idx_min], rand_list[idx_max] = rand_list[idx_max], rand_list[idx_min]

print(f'Массив после изменения: {rand_list}')
