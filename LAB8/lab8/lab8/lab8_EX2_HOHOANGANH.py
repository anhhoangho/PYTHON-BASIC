import numpy as np
import matplotlib.pyplot as plt

min_tem = 0
max_tem = 0
nhiet_do = {}
day = []
tem = []
with open("data.txt",'r') as file:
    for line in file:
        line = line.strip()
        if not line:
            continue

        ngay, do = line.split(",")
        ngay = int(ngay.strip())
        do = float(do.strip())

        day.append(ngay)
        tem.append(do)

# print(day)
# print(tem)

for i in tem:
    if min_tem == 0 or min_tem > i:
        min_tem = i
    if max_tem == 0 or max_tem < i:
        max_tem = i

# print(max_tem)
# print(min_tem)
# max_day = tem.index(max_tem)
# plt.annotate(f'Max: {temp_max}', xy=(max_y, temp_max))

max_day = tem.index(max_tem)
plt.text(max_day, max_tem, 'MAX', fontsize=8, color='red')
plt.plot(day, tem, color='k', linestyle='-', linewidth=2)
plt.xlabel('DAYS')
plt.ylabel('TEMPERATURES')

plt.show()