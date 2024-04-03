# Попов Юрий ИУ7-12Б
# Даны массивы D и F. Сформировать матрицу A по формуле
# ajk = sin(dj+fk)
# Определить среднее арифметическое положительных чисел каждой строки
# матрицы и количество элементов, меньших среднего арифметического.
# Результаты записать соответственно в массивы AV и L. Напечатать матрицу A в
# виде матрицы и рядом столбцы AV и L.
# В AV записывать особое значение при отсутствии положительных элементов
import math


def lst_input(n: int) -> list:
    lst = []
    for i in range(n):
        el = int(input(f'Введите {i + 1} элемент списка: '))
        lst.append(el)

    return lst


def average(string):
    positive_only = [el for el in string if el >= 0]
    if positive_only:
        return sum(positive_only) / len(positive_only)
    else:
        return None


lenn = int(input('Введите количество элементов в списке d: '))
d, f = lst_input(lenn), lst_input(lenn)

a = [[0] * lenn for i in range(lenn)]

for j in range(lenn):
    for k in range(lenn):
        a[j][k] = math.sin(d[j] + f[k])

av = []
l = []
for i in range(lenn):
    string = a[i]
    avg = average(string)
    if avg is not None:
        count = 0
        for j in range(lenn):
            if string[j] < avg:
                count += 1
        avg = format(avg, '.6g')

    else:
        count = None
    av.append(avg)
    l.append(count)

for i, line in enumerate(a):
    fmt = " ".join([f"{i:>8.6g}" for i in line])
    print(f"a[{i}] = {fmt}; {av[i]=}; {l[i]=}")
