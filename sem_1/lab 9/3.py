# Попов Юрий ИУ7-12Б
# Подсчитать в каждой строке матрицы D количество элементов, превышающих
# суммы элементов соответствующих строк матрицы Z. Разместить эти
# количества в массиве G, умножить матрицу D на максимальный элемент
# массива G. Напечатать матрицу Z, матрицу D до и после преобразования, а
# также массив G.

def input_matrix(n: int, name: str) -> list:
    """Ввод квадратной матрицы"""
    matx = []
    for i in range(n):
        el = list(map(int, input(f'Введите {i + 1} строку матрицы {name} : ').split()))
        matx.append(el)
    return matx


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

n = int(input('Введите размер матриц D и Z: '))

D = input_matrix(n, 'D')
print()
Z = input_matrix(n, 'Z')

G = []

for i, l in enumerate(D):
    count = 0
    summ = sum(Z[i])
    for el in l:
        if el > summ:
            count += 1
    G.append(count)


print('До преобразований')
print(output_matrix(D, 'D'))
print(output_matrix(Z, 'Z'))

maxx = max(G)
D = multipy_matrix(D, maxx)

print('После преобразований')
print(output_matrix(D, 'D'))
print(output_list(G, 'G'))