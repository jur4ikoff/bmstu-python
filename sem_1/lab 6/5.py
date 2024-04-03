import random

sp = list(map(int, input('Введите список: ').split())) or [int(random.randint(0, 100)) for _ in range(10)]
print(sp)

# Поменять местами элементы с характеристиками по варианту.
# Минимальный положительный и максимальный положительный.

minn = 10 ** 11
min_ind = -1

maxx = 0
maxx_ind = -1

for i in range(len(sp)):
    if sp[i] > maxx:
        maxx = sp[i]
        maxx_ind = i

    if sp[i] < minn:
        minn = sp[i]
        min_ind = i

sp[min_ind] = maxx
sp[maxx_ind] = minn

print(*sp)
for i, val in enumerate(sp):
    print(f"sp[{i}] = {val}")