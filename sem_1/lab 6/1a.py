sp = list(map(int, input('Введите список: ').split()))
print(sp)


'''1 задание'''
ind = int(input('Введите индекс элемента: '))
elem = int(input('Введите значение элемента: '))
sp.insert(ind, elem)


for i, val in enumerate(sp):
    print(f"lst[{i}] = {val}")
