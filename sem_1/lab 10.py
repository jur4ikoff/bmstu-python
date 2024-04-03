# Попов Юрий ИУ7-12б
# написать программу для вычисления приближённого значения интеграла
# известной, заданной в программе, функции двумя разными методами (правых прямоугольников, трапеций)

import math

func = lambda x: math.sin(x)  # Функция
primitive_func = lambda x: -1 * math.cos(x)  # Первобразная


def right_rectangles(func, start, finish, N):
    """Правило правых треугольников"""
    step = (finish - start) / N
    result = 0
    for i in range(N):
        result += func((i + 1) * step + start) * step
        result += func((i * step + (i + 1) * step) / 2 + start) * step
    return result


def middle_rectangles(func, start, finish, N):
    """Серединных прямоугольников"""
    step = (finish - start) / N
    result = 0
    for i in range(N):
        result += func((i * step + (i + 1) * step) / 2 + start) * step

    return result


def integrate_trapezoid(func, start, finish, N):
    """Правило трапеций"""
    step = (finish - start) / N
    result = 0
    for i in range(N):
        result += ((func((i + 1) * step + start) + func(i * step + start)) / 2) * step
    return result


def absolute_error(res_1: float, res_2: float) -> float:
    """res_2 - истинное значение, res_1 - измеренное"""
    return res_2 - res_1


def relative_error(res_1: float, res_2: float) -> float:
    """res_2 - истинное значение, res_1 - измеренное"""
    return ((res_2 - res_1) / res_2) * 100


def make_table(name1, name2, i1, i2, i3, i4, column_name_1, column_name_2):
    print('—' * 49)
    print(f"|{' ':^15}|{column_name_1:^15}|{column_name_2:^15}|")
    print('—' * 49)
    print(f"|{name1:^15}|{i1:^15.6g}|{i2:^15.6g}|")
    print('—' * 49)
    print(f"|{name2:^15}|{i3:^15.6g}|{i4:^15.6g}|")
    print('—' * 49)


def calculate_min_n(func, accuracy):
    N = 1
    integral_1 = func(N)
    N *= 2
    integral_2 = func(N)
    while abs(integral_1 - integral_2) < accuracy:
        integral = integral_2
        integral_2 = func(N * 2)
        N *= 2
    return N, integral_2


def main():
    start = float(input('Введите начальное значение: '))
    stop = float(input('Введите конечное значение значение: '))
    n1 = int(input('Введите количество участков разбиения N1: '))
    n2 = int(input('Введите количество участков разбиения N2: '))

    i1 = right_rectangles(func, start, stop, n1)
    i2 = right_rectangles(func, start, stop, n2)
    i3 = integrate_trapezoid(func, start, stop, n1)
    i4 = integrate_trapezoid(func, start, stop, n2)
    real_value = primitive_func(stop) - primitive_func(start)

    make_table('Метод 1', 'Метод 2', i1, i2, i3, i4, 'N1', 'N2')
    print()
    print(middle_rectangles(func, start, stop, n2))

    if abs(absolute_error(i2, real_value)) > abs(absolute_error(i4, real_value)):
        print(f'Метод трапеции более точный чем метод прямоугольников')
        less_func = lambda x: right_rectangles(func, start, stop, x)
    else:
        print(f'Метод прямоугольников более точный чем метод трапеций')
        less_func = lambda x: integrate_trapezoid(func, start, stop, x)

    make_table('Метод 1', 'Метод 2', absolute_error(i2, real_value), relative_error(i2, real_value),
               absolute_error(i4, real_value), relative_error(i4, real_value), 'Абсолютная погрешность',
               'Относительная погрешность')
    print()

    accuracy = float(input('Введите необходимую точность: '))
    minn_n, integral_value = calculate_min_n(less_func, accuracy)
    print(
        f'Для вычисления интеграла с точностью {accuracy}, нужно {minn_n:.6g} иттераций. \n Значение интеграла - {integral_value:.6g}')


if __name__ == '__main__':
    main()
