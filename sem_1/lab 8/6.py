# Попов Юрий ИУ7-12Б
# Транспонирование

n = int(input('Введите размер матрицы: '))

matx = []
for i in range(n):
    el = list(map(int, input(f'Введите {n} элемента матрицы: ').split()))
    matx.append(el)


for i in range(n):
    for j in range(i):
        matx[i][j], matx[j][i] = matx[j][i], matx[i][j]



for i, l in enumerate(matx):
    string = "".join([f"{e:^10}" for e in l])
    print(f"matrix[{i}] = {string}")