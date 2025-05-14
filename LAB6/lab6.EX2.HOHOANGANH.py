Month = ['Ja','Fe','Ma','Ap','May','June','Ju','Au','Sep','Oc','No','De']
count = 0
sum = 0
min = 0
max = 0
temp = []
for i in Month:
    n = int(input('enter temperature for {0}: '.format(i)))
    temp.append(n)
    if min == 0 or min > n:
        min = n
    if max == 0 or max < n:
        max = n
    sum += n
    count += 1

average = sum/count

print('The min is: ', min)
print('The max is: ', max)
print('The average is: ', round(average, 2))

print("The months with temperatures above average are:")
for i in range(len(Month)):
    if temp[i] > sum/12:
        print(f"{Month[i].capitalize()} ({temp[i]}°C)")