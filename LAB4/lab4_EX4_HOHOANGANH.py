# Hồ Hoàng anh - 22115054122103
tong = 0
score = input('enter your quarter scores: ')
score1 = score.split(' ')

# print(score1)

diem = []
for i in score1:
    score2 = float(i)
    diem.append(score2)

for y in diem:
    tong += y

tb = int(len(diem))
tong = round(tong/tb,2)

print('Your Final Score is: ', tong)
if tong < 7:
    print('Rating: Fair')
elif tong < 10:
    print('Rating: Poor')
elif tong < 16:
    print('Rating: Good')
elif tong <19:
    print('Rating: Very Good')
else:
    print('Rating: Outstanding')








