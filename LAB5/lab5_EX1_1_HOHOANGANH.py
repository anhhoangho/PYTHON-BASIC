# Hồ Hoàng anh - 22115054122103

import random

sum = 0
count = 0

a = int(input('Nhập tổng số cho short: '))
b = int(input('Nhập tổng số cho long: '))
c = input('Enter your file path: ')

with open('short_hhanh.txt', 'w') as short:
    for i in range(a):
        so_short = random.randint(51, 99)
        short.write('{0}\n'.format(so_short))
with open('long_hhanh.txt', 'w') as long:
    for j in range(b):
        so_long = random.randint(0, 50)
        long.write('{0}\n'.format(so_long))

with open(c, 'r') as f:
    for line in f:
        n = int(line.strip())
        sum += n
        count += 1
        # print(line)

average = sum/count
print('Count: ', count, end=', ')
print('Average: ', average)

short.close()
long.close()