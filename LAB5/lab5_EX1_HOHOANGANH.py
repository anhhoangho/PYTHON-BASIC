# Hồ Hoàng anh - 22115054122103

a = input('Enter your file path: ')

sum = 0
count = 0
with open(a, 'r') as f:
    for line in f:
        n = int(line.strip())
        sum += n
        count += 1
        print(line)

average = sum/count
print('Count: ', count, end=', ')
print('Average: ', average)

