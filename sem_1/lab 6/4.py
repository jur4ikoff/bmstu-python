import random

sp = list(map(int, input('Введите список: ').split())) or [int(random.randint(0, 100)) for _ in range(1000)]
print(sp)

maxx = max(sp)

primes = [True] * (maxx + 1)
primes[0] = primes[1] = False
for i in range(2, int(maxx) + 1):
    if primes[i]:
        primes[i * i: maxx + 1: i] = [False] * len(primes[i * i: maxx + 1: i])
primes = [p for p in range(maxx + 1) if primes[p]]

sequence = []
seq_len = 0
cur = []
cur_len = 0

for i in range(len(sp)):
    if sp[i] in primes:
        cur_len += 1
        cur.append(sp[i])
    else:
        if cur_len > seq_len:
            sequence = cur
            seq_len = cur_len
            cur = []
            cur_len = 0
        else:
            cur = []
            cur_len = 0

for i, val in enumerate(sequence):
    print(f"элемент последовательности {i} = {val}")

print(f'длина последовательности - {seq_len}')


