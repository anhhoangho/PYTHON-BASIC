# Hồ Hoàng anh - 22115054122103

so = input('Your numbers: ')
so1 = so.split(' ')
so2 = []
for i in so1:
    y = int(i)
    so2.append(y)

print('min = ', min(so2), end=' ')
print('max = ', max(so2))

