# Hồ Hoàng anh - 22115054122103

number = []
while len(number) < 5:
    a = int(input('Enter a number: '))
    if a in number:
        print('{0} is already in the bag'.format(a))
    else:
        number.append(a)

print('Your Bag: ', number)