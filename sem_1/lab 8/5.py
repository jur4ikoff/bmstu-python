# Попов Юрий ИУ7-12Б
# Найти максимальное значение в квадратной матрице над главной диагональю и
# минимальное - под побочной диагональю.

n = int(input('Введите размер матрицы: '))

matx = []
for i in range(n):
    el = list(map(int, input(f'Введите {n} элемента матрицы: ').split()))
    matx.append(el)

maxx = 0
minn = 10 ** 9

for i in range(n):
    for j in range(i):
        maxx = max(maxx, matx[j][i])

for x in range(len(matx[0])):
    for y in range(n - x, n):
        minn = min(minn, matx[y][x])

print(f'Минимальный элемент: {minn}')
print(f'Максимальный элемент: {maxx}')
