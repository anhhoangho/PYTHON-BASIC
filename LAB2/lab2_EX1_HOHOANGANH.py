# Hồ Hoàng anh - 22115054122103

from random import randint

x = randint(100,999)
y = randint(100,999)
print(" ",x, '\n+',y)

c = x+y
print(" ----- (enter the result)")
kq = float(input())

if kq == c:
    print('Good Answer')
else:
    print('wrong answer, correct answer is ', c)

# import random
# a = print(random.randint(90:100))
# import toàn bộ thư viện