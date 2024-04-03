# Попов Юрий ИУ7-12Б
# Сформировать матрицу C путём построчного перемножения матриц A и B
# одинаковой размерности (элементы в i-й строке матрицы A умножаются на
# соответствующие элементы в i-й строке матрицы B), потом сложить все
# элементы в столбцах матрицы C и записать их в массив V. Напечатать матрицы
# A, B, C и массив V.


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


n = int(input('Введите размер матриц A и B: '))

A = input_matrix(n, 'A')
B = input_matrix(n, 'B')
C = []

for i in range(n):
    d = []
    for j in range(n):
        d.append(A[i][j] * B[i][j])
    C.append(d)

V = []
for i in range(n):
    summ = 0
    for j in range(n):
        summ += C[j][i]
    V.append(summ)


output_matrix(A, "A")
print()
output_matrix(B, "B")
print()
output_matrix(C, "C")
print()
output_list(V, "V")