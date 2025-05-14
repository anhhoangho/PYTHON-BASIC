# Hồ Hoàng Anh - 22115054122103
print("Welcome to the Temperature Counter")

file = input("Enter the path of the temperature file: ")
temps = []
with open(file, 'r') as f:
    for line in f:
        temp = line.split()[1]
        temps.append(float(temp))

for t in sorted(set(temps)):
    print(f"{t:.1f} : {temps.count(t)}")

print("Thank you for using the Temperature Counter")

