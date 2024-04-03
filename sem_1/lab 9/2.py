# Попов Юрий ИУ7-12Б
# Повернуть квадратную целочисленную матрицу на 90 градусов по часовой
# стрелке, затем на 90 градусов против часовой стрелки. Вывести исходную,
# промежуточную и итоговую матрицы. Дополнительных матриц и массивов не
# вводить. Транспонирование не применять.

def input_matrix(n: int) -> list:
    """Ввод квадратной матрицы"""
    matx = []
    for i in range(n):
        el = list(map(int, input(f'Введите {i + 1} строку матрицы: ').split()))
        matx.append(el)
    return matx


def output_matrix(matx):
    """Вывод матрицы"""
    output_string = ''
    for i, string in enumerate(matx):
        output = ''.join([f"{s:^6.6g}" for s in string])
        output_string += f'matrix[{i + 1}] = {output}\n'
    return output_string


def rotate_right(mat: list):
    return tuple(zip(*mat[::-1]))


def rotate_left(mat: list):
    return tuple(zip(*mat))[::-1]


n = int(input('Введите размер квадратной матрицы: '))
matrix = input_matrix(n)

print('Исходная матрица')
print(output_matrix(matrix))
print()

matrix = rotate_right(matrix)
print('Промежуточная матрица')
print(output_matrix(matrix))
print()

matrix = rotate_left(matrix)
print('Итоговая матрица')
print(output_matrix(matrix))
print()