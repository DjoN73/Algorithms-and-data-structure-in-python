from random import randint

rand_list = [randint(0, 50) for _ in range(100)]
print(rand_list)
count_num = {i: 0 for i in rand_list}

for idx in rand_list:
    if idx in count_num:
        count_num[idx] += 1
print(count_num)

v = list(count_num.values())
k = list(count_num.keys())

print(f"Чаще всего встречается число: {k[v.index(max(v))]}")
