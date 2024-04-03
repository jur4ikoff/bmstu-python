# Попов Юрий ИУ7-12Б
# Дана матрица символов. Заменить в ней все гласные английские буквы на
# точки. Напечатать матрицу до и после преобразования.

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


vowels = "aouei"
len_d = int(input('Введите размер матрицы: '))
matrix = input_matrix(len_d, 'matrix')
print('До:')
output_matrix(matrix, "matrix")

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        try:
            if matrix[i][j].lower() in vowels:
                matrix[i][j] = "."
        except AttributeError:
            pass

print('После:')
output_matrix(matrix, "matrix")
