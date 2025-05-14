# Hồ Hoàng anh - 22115054122103

while True:
    n = int(input('enter a positive integer: '))
    if n > 0:
        break

s = 0
for i in range(n+1):
    s = s + i
n = str(n)
print('the sum 1+...+{0} is {1}'.format(n, s))