import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings(action="ignore")

lst = []
s = 0
count = 0
with open("dataset.txt") as f:
    while True:
        try:
            line = float(f.readline().strip().replace(',', '.'))
            count += 1
            s += line
        except:
            line = ''
        if not line:
            break
        lst.append(line)

sr = round(s / count, 2)

dataset = pd.DataFrame({'x': lst})
x_sr = [round(i - sr, 2) for i in lst]
x_sr_2 = [round(i ** 2, 2) for i in x_sr]
dataset.insert(loc=len(dataset.columns), column='x-sr', value=x_sr)
dataset.insert(loc=len(dataset.columns), column='(x-sr)**2', value=x_sr_2)

minn = dataset["x"].min()
maxx = dataset["x"].max()
delta = 0.05
cur = round(minn, 1)
next = cur + 0.05
names = []
values = []
while cur < maxx:
    key = round(cur, 2)
    next = round(next, 2)
    count = dataset.query('@key <= x < @next').shape[0]
    names.append(key)
    values.append(count)
    cur += delta
    next += delta

#names = [i * 10 for i in names]
values[-1] += 1
dict_n = {"names": names, "values": values}
print(dict_n)
new_dataset = pd.DataFrame(dict_n)
print(new_dataset)

# seaborn histogram

# seaborn histogram
# sns.distplot(dataset['x'], hist=True, kde=True,
#             bins=180 // 10, color='darkblue',
#             hist_kws={'edgecolor': 'black'},
#             kde_kws={'linewidth': 4})
# Add labels
plt.bar(new_dataset['names'], new_dataset['values'], width=0.05, edgecolor="black", align="edge")
plt.axvline(sr, color='r', linestyle='--', label=f'Среднее = {sr}')
plt.xlabel('Время')
plt.ylabel('Количество вхождений')
plt.xticks(new_dataset['names'])
plt.show()
