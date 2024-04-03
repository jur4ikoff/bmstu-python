# Попов Юрий ИУ7-12Б
# После каждого элемента целочисленного списка, имеющего свойство по
# варианту, добавить его удвоенное значение, без использования вложенных
# циклов. Без insert append срезов

# Чётные элементы

import random

# sp = []
# for i in range(int(input())):
#     el = int(input())
#     sp.append(el)


sp = [int(random.randint(0, 10)) for i in range(5)]
print(sp)

lenn = len(sp)
indexs = []
a = 1
for i in range(len(sp)):
    if sp[i] % 2 == 0:
        indexs.append(i + a)
        a += 1

sp += [0] * (a - 1)
a -= 1

c = 0
print(indexs)
for i in range(len(sp)):
    if i in indexs:
        sp[lenn + c] = sp[i - 1] * 2
        need_ind = lenn + c
        for j in range(need_ind - 1,  indexs[c] - 1, -1):
            sp[j], sp[j + 1] = sp[j + 1], sp[j]
        c += 1
print(sp)
