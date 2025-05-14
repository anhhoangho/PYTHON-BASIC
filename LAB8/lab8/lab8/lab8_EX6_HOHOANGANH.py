# Hồ Hoàng Anh -22115054122103
import numpy as np
import matplotlib.pyplot as plt
import csv

count = 0
name = []
x = []
y = []
file1 = input('Enter the path of the data file: ')
with open(file1, 'r') as file:
    doc = csv.reader(file)
    for row in doc:
        count += 1
        name.append(row[0])
        x.append(float(row[1]))
        y.append(float(row[2]))


n = len(y)
for i in range(n - 1):
    for j in range(i + 1, n):
        if y[i] > y[j]:
            temp = y[i]
            y[i] = y[j]
            y[j] = temp

            temp = x[i]
            x[i] = x[j]
            x[j] = temp

            temp = name[i]
            name[i] = name[j]
            name[j] = temp

for i in range(n):
    print(f"{name[i]},{x[i]},{y[i]}")

with open("oilwell3_new", 'w', newline='') as file:
    writer = csv.writer(file)
    for i in range(count):
        writer.writerow([name[i], y[i], x[i]])

# print(name)
# print(x)
# print(y)

if count % 2 == 0:
    giua1, giua2 = count // 2 - 1, count // 2
    y_trung_vi = (y[giua1] + y[giua2]) / 2
    print(giua1)
    print(giua2)
else:
    giua_le = count // 2
    y_trung_vi = y[giua_le]
    print(giua_le)


plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='blue')
plt.axhline(y=y_trung_vi, color="red", linewidth=2, alpha=0.5, label=f'Trung vị Y = {y_trung_vi:.2f}')

for i, txt in enumerate(name):
    plt.annotate(txt, (x[i], y[i]), textcoords="offset points", xytext=(5, 5), ha='center')

for i in range(count):
    plt.plot([x[i], x[i]], [y[i], y_trung_vi], color='blue', linestyle='-', linewidth=1)


plt.title("Pipeline")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.grid(True)
plt.legend()
plt.show()
