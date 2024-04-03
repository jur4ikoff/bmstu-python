# Попов Юрий ИУ7-12Б
# Найти строку, имеющую определённое свойство по варианту. наибольшое среднее


n = int(input('Введите размер матрицы: '))

matx = []
for i in range(n):
    el = list(map(int, input(f'Введите {n} элемента матрицы: ').split()))
    matx.append(el)

ind = -1
maxx = 0
for i in range(n):
    el = matx[i]
    sr = sum(el) /  n
    if sr > maxx:
        maxx = sr
        ind = i

print(f'Максимальный элемент матрицы {matx[ind]}')