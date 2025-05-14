import numpy as np
import matplotlib.pyplot as plt

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

print(day)
print(tem)


plt.plot(day, tem, color='k', linestyle='-', linewidth=2)
plt.xlabel('DAYS')
plt.ylabel('TEMPERATURES')
# plt.legend('tem')

plt.show()
