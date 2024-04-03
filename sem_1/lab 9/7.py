# Попов Юрий ИУ7-12Б
# Ввести трёхмерный массив (массив матриц размера X*Y*Z), вывести из него i-й
# срез (матрицу - фрагмент трёхмерного массива) по второму индексу (нумерация
# индексов начинается с 1).


def output_matrix(matx, name: str):
    """Вывод матрицы"""
    output_string = ''
    for i, string in enumerate(matx):
        output = ''.join([f"{s:^6.6g}" for s in string])
        output_string += f'{name}[{i + 1}] = {output}\n'
    return output_string


def input_3d_matrix(lst, x, y, z):
    for i in range(x):
        for j in range(y):
            for k in range(z):
                el = int(input(f"Введите {(i, j, k)} элемент: "))
                lst[i][j][k] = el
    return lst


X, Y, Z = map(
    int, input("Введите размеры трехмерного списка: ").split()
)

lst = [[[0 for k in range(Z)] for j in range(Y)] for i in range(X)]
lst = input_3d_matrix(lst, X, Y, Z)

t = int(input("Введите i: "))
t -= 1
try:
    print(output_matrix(lst[t], f"lst[{t}]"))
except IndexError:
    print('Неверный i')