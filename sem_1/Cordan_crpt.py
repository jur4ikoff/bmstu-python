import math
import random
import numpy as np

n = 3
# for i in range(n):
#    el = [random.randint(1, 4) for _ in range(n)]
#    matx.append(el)

matx = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def rotate_right(mat: list):
    return list(zip(*mat[::-1]))


a = matx
b = rotate_right(a)
c = rotate_right(b)
d = rotate_right(c)

line1 = []
for i in range(n):
    el = a[i] + list(b[i])
    line1.append(el)

line2 = []
for i in range(n):
    el = list(c[i]) + list(d[i])
    line2.append(el)

matx = [line1 + line2][0]
print(matx)


def delete_from_matrix(matx):
    for k in range(1, 10):
        number = random.randint(0, 3)
        if number == 0:
            for i in range(0, n):
                for j in range(0, n):
                    if matx[i][j] == k:
                        matx[i][j] = 0
        if number == 1:
            for i in range(0, n):
                for j in range(n, 2 * n):
                    if matx[i][j] == k:
                        matx[i][j] = 0
        if number == 2:
            for i in range(n, 2 * n):
                for j in range(0, n):
                    if matx[i][j] == k:
                        matx[i][j] = 0

        if number == 3:
            for i in range(n, 2 * n):
                for j in range(n, 2 * n):
                    if matx[i][j] == k:
                        matx[i][j] = 0
    return matx


matx = delete_from_matrix(matx)
print(matx)

s = 'Шла саша по шоссе'
new_matx = [[0 for _ in range(6)] for _ in range(6)]

for i in range(2 * n):
    for j in range(2 * n):
        if matx[i][j] == 0:
            el = s[0]
            s = s[1:]

