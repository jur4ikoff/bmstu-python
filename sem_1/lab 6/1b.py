import random

# sp = list(map(int, input('Введите список: ').split())) or [int(random.randint(0, 1000)) for _ in range(10)]
sp = []
for i in range(n:=int(input("Введите количество элементов: "))):
    el = int(input(f"Введите элемент {i+1}: "))
    sp.append(el)
print(sp)

ind = int(input('Введите индекс элемента: '))
elem = int(input('Введите значение элемента: '))
new_sp = []
for i in range(n):
    if i == ind:
        new_sp.append(elem)
        new_sp.append(sp[i])
    else:
        new_sp.append(sp[i])


if ind > n:
    new_sp.append(elem)
if n <= 0:
    new_sp = [elem]
sp = new_sp

del new_sp

for i, val in enumerate(sp):
    print(f"lst[{i}] = {val}")
