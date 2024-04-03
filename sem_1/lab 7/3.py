# Попов Юрий ИУ7-12Б
# Поиск элемента с наибольшим числом английских гласных букв


# sp = []
# for i in range(int(input('Введите кол-во элементов списка'))):
#     el = input()
#     sp.append(el)

sp = ['asdfg', 'ujkythtgrfdwsx', 'u7gfhdffsnjmfghjsgjkmdfat', 'htfgsdfghgsgsgf']

glas = ['a', 'A', 'e', 'A', 'i', 'I', 'o', 'O', 'u', 'U', 'y', 'Y']

count = 0
el = 0
for i in range(len(sp)):
    cur = 0
    for j in range(len(sp[i])):
        if [sp][i][j] in glas:
            cur += 1

    if cur > count:
        el = i
        count = cur

print(f'Максимальное количество согласных: {count}, в строке: {el}')
