import math

func = lambda x: math.sin(x)
a, b = list(map(float, input("Введите a, b: ").split()))
EPS = 10 ** -5
max_count = 10 ** 6
c = (a + b) / 2
count = 0
while b - a > EPS:
    count += 1
    if count > max_count:
        print("count > max_counts")
        break

    if abs(b - a) < EPS:
        break

    fa = func(a)
    c = (a + b) / 2
    fc = func(c)

    if fa * fc < 0:
        b = c
    else:
        a = c

print(a)
