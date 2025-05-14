# Hồ Hoàng anh - 22115054122103

even = []
odd = []
while True:
    number = input('your numbers:')
    numbers = number.split(' ')
    for x in numbers:
        x = int(x)
    if x == 0:
        break
    elif x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)

print('The odd numbers you entered: ',odd)
print('The even numbers you entered: ',even)