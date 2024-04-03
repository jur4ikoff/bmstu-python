import random

sp = list(map(int, input('Введите список: ').split())) or [int(random.randint(0, 1000)) for _ in range(10)]
print(sp)

k = int(input('Введите номер экстремума: '))

flag = True
count = 0
for i in range(1, len(sp) - 1):
    if (sp[i] > sp[i + 1] and sp[i] > sp[i - 1]) or (sp[i] < sp[i + 1] and sp[i] < sp[i - 1]):
        count += 1

    if count == k:
        print(f'Номер k экстремума - {sp[i]}')
        flag = False
        break

if flag:
    print('В списке нет K-го экстремума')