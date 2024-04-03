import sympy as sp
import numpy as np
# Найти когда приращение функции и производная больше нуля на отрезке
func = lambda x: 10 * x ** 2 + 10 * x + 4  # менять функцию тут
a, b = map(int, input("Введи шаг начала и конца: ").split())
H = 100  # шаг разбиения
steps = np.linspace(a, b, H)

x = sp.symbols('x')
f = 10 * x ** 2 + 10 * x + 4
derivative_func = sp.lambdify(x, sp.diff(f, x), 'numpy')

# Вычисляем значение производной в точке

# Значение производной в точке
last = func(steps[0])
count = 0
if derivative_func(steps[0]) >= 0:
    for i in range(1, len(steps) - 1):
        cur = func(steps[i])
        diff = derivative_func(steps[i])
        if cur - last >= 0 and diff >= 0:
            count += 1
        last = cur

    if count == 98:
        print('Условия соблюдены')
    else:
        print("Условия не соблюдены")
else:
    print("Условия не соблюдены")
