# Попов Юрий ИУ7-12Б
# Переставить местами строки с наибольшим и наименьшим количеством
# отрицательных элементов

n = int(input('Введите размер матрицы: '))

matx = []
for i in range(n):
    el = list(map(int, input(f'Введите {n} элемента матрицы: ').split()))
    matx.append(el)


ind = -1
minn = 10 ** 9
for i in range(n):
    negativ_count = 0
    for j in range(n):
        if matx[j][i] < 0:
            negativ_count += 1

    if negativ_count < minn:
        ind = i
        minn = negativ_count
print('')
print(f'Индекс столбца - {ind}')
for i in range(n):
    print(f'строка {i}, элемент - {matx[i][ind]}')
