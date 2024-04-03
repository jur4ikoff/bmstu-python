# Попов Юрий ИУ7-12Б
# Удалить все элементы целочисленного списка, имеющие свойство по варианту,
# за один цикл. Без del pop remove срезов

# нечетные элементы


import random

# sp = []
# for i in range(int(input())):
#     el = int(input())
#     sp.append(el)

sp = [int(random.randint(0, 100)) for i in range(10)]
print(sp)

col = 0
for i in range(len(sp)):
    if sp[i] % 2 == 1:
        for j in range(i - 1, col - 1, -1):
            sp[j], sp[j + 1] = sp[j + 1], sp[j]
        col += 1

sp = sp[col:]

for i, el in enumerate(sp):
    print(f"sp[{i}]={el}")
