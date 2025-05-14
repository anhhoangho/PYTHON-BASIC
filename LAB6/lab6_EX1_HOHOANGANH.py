city = input("Input you file: ").strip()

with open(city, "r") as f:
    a = f.readlines()
temp1 = []
cities = []
for i in a:
    city, temp = i.rstrip().split(" ")
    temp = float(temp)
    cities.append((city, temp))
    temp1.append((temp, city))


cities.sort()
for c, t in cities:
    print(f"{c:<10}{t:<10.1f}")
temp1.sort()
for t, c in temp1:
    print(f"{t:<10.1f}{c:<10}")