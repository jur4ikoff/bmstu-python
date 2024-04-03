x, eps = map(float, input().split())
x = int(x)
summ = 0
k = 0
cur = 10 ** 6
n = 1
while abs(cur) > eps:
    n += 1
    cur = ((-1) ** n) * (n ** 2 * x) / (n ** 2 - 1)
    print(cur)
    summ += cur
    print(summ)
