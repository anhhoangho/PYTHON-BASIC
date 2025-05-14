import matplotlib.pyplot as plt
y= []
x=[]
# Open file

with open("scores.txt", 'r') as infile:
    for line in infile:
        line = line.strip()
        if not line:
            continue
        values = line.split(";")
        x.append(values[0])
        y.append(values[2])

        for i in y:
            i = i.strip()
            if not i:
                continue
        value = i.split(";")
print(i)
print(y)

# x = list(range(10, len(y)))
plt.plot(x,y)
plt.xlabel("ID")
plt.ylabel("scores")
plt.title("Exam1")
plt.show()