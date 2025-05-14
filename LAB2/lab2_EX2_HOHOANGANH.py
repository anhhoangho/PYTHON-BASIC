# Hồ Hoàng anh - 22115054122103

leng1 = float(input('Length of rectangle 1: '))
wid1 = float(input('Width of rectangle 1: '))
leng2 = float(input('Length of rectangle 2: '))
wid2 = float(input('Width of rectangle 2: '))

cv1 = leng1 * wid1
cv2 = leng2 * wid2

if cv1 > cv2:
    print('Rectangle 1 is bigger')
elif cv1 < cv2:
    print('Rectangle 2 is bigger')
else:
    print('rectangle 1 and 2 have the same area')

