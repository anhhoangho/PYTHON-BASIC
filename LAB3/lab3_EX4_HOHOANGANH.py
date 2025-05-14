# Hồ Hoàng anh - 22115054122103

while True:
    n = int(input('enter a positive integer: '))
    if n > 0:
        break


fn = 1
fn_1 = 1

for x in range(3, n+1):
    tmp = fn + fn_1
    fn = fn_1
    fn_1 = tmp

cuoi = 'th'

if n<11 or n>13:
    last = n % 10
    if last == 1:
        cuoi = 'st'
    if last == 2:
        cuoi = 'nd'
    if last == 3:
        cuoi = 'rd'

print('the {0}{1} Fibonacci number is {2}'.format(n, cuoi,tmp))

