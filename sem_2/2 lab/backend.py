# Поиск корней методом секущих
# Выполнил Попов Ю.А. ИУ7-22Б
# ЛР2

import math
import numpy as np
from matplotlib import pyplot as plt


def secant_method(f, a, b, eps, Nmax) -> tuple:
    if f(a) * f(b) > 0:
        return None, -1, 1

    x0 = a
    x1 = b
    n = 1

    while abs(f(x1)) > eps and n < Nmax:
        x_next = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))
        x0 = x1
        x1 = x_next
        n += 1

    if n == Nmax:
        return None, n, 2
    else:
        return x1, n, 0


def make_table(table):
    print()
    print(f"{'Таблица корней':^107}")
    print('—' * 107)
    print(f"|{'№ корня':^10}|{'интервал':^25}|{'x':^20}|{'f(x)':^20}|{'Iteration count':^15}|{'Error Code':^10}|")
    print('—' * 107)

    for i in range(len(table)):
        print(
            f"|{table[i][0]:^10}|{f'[{table[i][1][0]:^6.6g};{table[i][1][1]:^6.6g}]':^25}|{table[i][2]:^20.7g}|{table[i][3]:^20.7g}|{table[i][4]:^15}|{table[i][5]:^10}|")
    print('—' * 107)

    return ""


def find_extremums(x_axis: list, y_axis: list) -> list:
    extremums = []
    for i in range(1, len(x_axis) - 1):
        if y_axis[i - 1] < y_axis[i] and y_axis[i] > y_axis[i + 1]:
            extremums.append((x_axis[i], y_axis[i]))
        elif y_axis[i - 1] > y_axis[i] and y_axis[i] < y_axis[i + 1]:
            extremums.append((x_axis[i], y_axis[i]))

    return extremums


def find_inflection_points(x_axis: list, y_axis: list) -> list:
    inflection_points = []
    for i in range(2, len(y_axis) - 2):
        if (y_axis[i] - 2 * y_axis[i - 1] + y_axis[i - 2]) * (
                y_axis[i] - 2 * y_axis[i + 1] + y_axis[i + 2]
        ) < 0:  # Проверяем условие точки перегиба
            inflection_points.append((x_axis[i], y_axis[i]))

    return inflection_points


def create_graph(f, a, b, n, result):
    x = np.linspace(a, b, n * 10)
    y = list(map(f, x))
    plt.plot(x, y)
    plt.title('График функции')
    plt.xlabel('x')
    plt.ylabel('f(x)')

    extremums = find_extremums(x, y)
    inflections = find_inflection_points(x, y)
    try:
        if extremums:
            plt.scatter(*zip(*extremums), color='red', label='Extremum')
        else:
            print("No Extremum on interval")
        if inflections:
            plt.scatter(*zip(*inflections), color='green', label='Inflection point')
        else:
            print("No inflection on interval")
        if result:
            plt.scatter(*zip(*[[el[2], el[3]] for el in result]), color='blue', label='Solution')
        else:
            print("No solutions on interval")
    except Exception as e:
        print(e)
    plt.grid(True)
    plt.legend()
    plt.show()


def calculate(func, a, b, h, eps, n_max, ):
    result = []
    n = math.ceil((b - a) / h)

    for i in range(1, n + 1):
        x0 = a + h * (i - 1)
        x1 = a + h * i
        res, iterations, exit_code = secant_method(func, x0, x1, eps, n_max)
        # if n > 50:
        if isinstance(res, (float, int)):
            result.append([i, (x0, x1), round(res, 6), round(func(res), 6), iterations, exit_code])

    make_table(result)
    create_graph(func, a, b, n, result)
    return result
