# Hồ Hoàng anh - 22115054122103


a = input('Enter your file path: ')

count = 0
sum = 0
min = 0
max = 0

with open(a, 'r') as f:
    for line in f:
        n = int(line.strip())
        if min == 0 or min > n:
            min = n
        if max == 0 or max < n:
            max = n
        sum += n
        count += 1
        # print(line)
average = sum/count

print('The min is: ', min)
print('The max is: ', max)
print('The average is: ', round(average, 2))


