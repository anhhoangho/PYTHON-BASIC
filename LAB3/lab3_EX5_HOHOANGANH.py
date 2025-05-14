# Hồ Hoàng anh - 22115054122103
count = 0
min = 0
max = 0
sum = 0
while True:
    a = int(input('enter the interger or 0 to exit: '))
    if a == 0:
        break
    count += 1
    if min == 0 or min > a:
        min = a
    if max == 0 or max < a:
        max = a
    sum += a

print('you entered {0} values'.format(count))
print('the min and max you entered are {0} and {1}'.format(min, max))
print('The sum is ', sum)
aver = sum/count
print('the average is ', round(aver,2))



