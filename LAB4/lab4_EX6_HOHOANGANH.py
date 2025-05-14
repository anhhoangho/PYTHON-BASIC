# Hồ Hoàng anh - 22115054122103

chu = []
a = input('Enter strings separated by exactly one spcae: ')
a1 = a.split(' ')
for i in a1:
    if i in chu:
        continue
    else:
        chu.append(i)

print('Your Bag: ', chu)


