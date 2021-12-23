result = {}
for i in range(2, 10):
    result[i] = []
    for j in range(2, 100):
        if j % i == 0:
            result[i].append(j)
    print(f'Для числа {i} количество кратных чисел: {len(result[i])}. Кратные числа {result[i]}')
