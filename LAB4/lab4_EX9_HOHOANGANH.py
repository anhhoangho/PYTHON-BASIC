# Hồ Hoàng anh - 22115054122103
from random import randint
loto = []
while len(loto) < 5:
    x = randint(1,49)
    loto.append(x)
    loto.sort()
    y = randint(1,10)

print('Your Loto: ',end=' ')
for i in loto:
    print(i, end=' ')
print('- ', y, end=' ')