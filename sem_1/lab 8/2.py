# Попов Юрий ИУ7-12Б
# Переставить местами строки с наибольшим и наименьшим количеством
# отрицательных элементов

n = int(input('Введите размер матрицы: '))

matx = []
for i in range(n):
    el = list(map(int, input(f'Введите {n} элемента матрицы: ').split()))
    matx.append(el)

maxx_count = 0
ind_max = 0
ind_min = 0
min_count = 10 ** 6

for i in range(n):
    count = 0
    for j in range(n):
        if matx[i][j] < 0:
            count += 1

        if count > maxx_count:
            maxx_count = count
            ind_max = i

        if count < min_count:
            min_count = count
            ind_min = i


for i in range(n):
    matx[ind_max][i], matx[ind_min][i] = matx[ind_min][i], matx[ind_max][i]


for i, l in enumerate(matx):
    string = "".join([f"{e:^10}" for e in l])
    print(f"matrix[{i}] = {string}")