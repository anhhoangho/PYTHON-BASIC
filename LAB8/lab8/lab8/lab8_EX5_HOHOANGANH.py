import matplotlib.pyplot as plt

y = []
x = []

# Mở file để đọc
with open("scores.txt", 'r') as infile:
    for line in infile:
        line = line.strip()
        if not line:
            continue
        values = line.split(";")
        x.append(values[0])
        scores = values[2].split(",")
        y.append([float(score) for score in scores])

print(x)
print(y)

y_1 = [scores[0] for scores in y]


plt.plot(x, y_1, marker='o', linestyle='-', color='b')

plt.xlabel("ID")
plt.ylabel("First Score")
plt.title("First Exam Score for Each ID")
plt.show()
