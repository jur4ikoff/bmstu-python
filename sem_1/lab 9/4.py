# Попов Юрий ИУ7-12Б
# Задана матрица D и массив I, содержащий номера строк, для которых
# необходимо определить максимальный элемент. Значения максимальных
# элементов запомнить в массиве R. Определить среднее арифметическое
# вычисленных максимальных значений. Напечатать матрицу D, массивы I и R,
#  среднее арифметическое значение.


def input_matrix(n: int, name: str) -> list:
    """Ввод квадратной матрицы"""
    matx = []
    for i in range(n):
        el = list(map(int, input(f'Введите {i + 1} строку матрицы {name} : ').split()))
        matx.append(el)
    return matx


def input_lst(n: int, name: str) -> list:
    lst = []
    for i in range(n):
        el = int(input(f'Введите {i + 1} элемент списка {name}: '))
        lst.append(el)

    return lst


def output_matrix(matx, name: str):
    """Вывод матрицы"""
    output_string = ''
    for i, string in enumerate(matx):
        output = ''.join([f"{s:^6.6g}" for s in string])
        output_string += f'{name}[{i + 1}] = {output}\n'
    return output_string


def output_list(list, name: str):
    """Вывод листа"""
    output_string = ''
    for i, s in enumerate(list):
        output_string += f'{name}[{i + 1}] = {s:^6.6g}\n'
    return output_string


def multipy_matrix(matx, k):
    """Умножение матрицы случайного опзинп"""
    for i in range(len(matx)):
        for j in range(len(matx[i])):
            matx[i][j] *= k

    return matx


len_d = int(input('Введите размер матрицы D: '))
D = input_matrix(len_d, 'D')

len_l = int(input('Введите размер массива l: '))
l = input_lst(len_l, 'l')

R = []
for i in l:
    try:
        R.append(max(D[i]))
    except IndexError:
        pass

avg = sum(R) / len(R)

output_matrix(D, "D")
output_list(l, "l")
output_list(R, "R")
print(f"Среднее арифмитическое: {avg:.6g}")
