# Попов Юрий ИУ7-12Б
# Замена двух подряд идущих цифр на последнюю цифру их суммы

import random
# sp = []
# for i in range(int(input('Введите кол-во элементов списка'))):
#     el = input()
#     sp.append(el)

sp = [int(random.randint(0, 5)) for i in range(10)]
print(sp)

for i in range(len(sp) - 1):
    if sp[i] == sp[i + 1]:
        summ = sp[i] + sp[i + 1]
        sp[i] = int(str(summ)[-1])
        sp[i + 1] = -1

col = 0
for i in range(len(sp)):
    if sp[i] == -1:
        for j in range(i - 1, col - 1, -1):
            sp[j], sp[j + 1] = sp[j + 1], sp[j]
        col += 1

sp = sp[col:]
print(sp)



