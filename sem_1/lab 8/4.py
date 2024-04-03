# Попов Юрий ИУ7-12Б
# Переставить местами столбцы с максимальной и минимальной суммой
# элементов.

n = int(input('Введите размер матрицы: '))

matx = []
for i in range(n):
    el = list(map(int, input(f'Введите {n} элемента матрицы: ').split()))
    matx.append(el)

maxx_summ = 0
ind_max = 0
ind_min = 0
min_summ = 10 ** 6


for i in range(n):
    summ = 0
    for j in range(n):
        summ += matx[j][i]

    if summ > maxx_summ:
        ind_max = i
        maxx_summ = summ

    if summ < min_summ:
        ind_min = i
        min_summ = summ

for i in range(n):
    matx[i][ind_max], matx[i][ind_min] = matx[i][ind_min], matx[i][ind_max]

for i, l in enumerate(matx):
    string = "".join([f"{e:^10}" for e in l])
    print(f"matrix[{i}] = {string}")





