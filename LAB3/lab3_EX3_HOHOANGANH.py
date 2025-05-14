# Hồ Hoàng anh - 22115054122103

while True:
    n = int(input('enter a positive integer: '))
    if n > 0:
        break

s = 1
for i in range(1, n+1):
    s = s * i

print(s)