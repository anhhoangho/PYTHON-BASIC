# Hồ Hoàng anh - 22115054122103

n = int(input('Số số nguyên tố là: '))

n_to = []
dau = 2

while len(n_to) < n:
    dung = True
    for i in range(2, int(dau**0.5)+1):
        if dau % i ==0:
            dung = False
            break
    if dung:
        n_to.append(dau)
    dau+=1
print(n_to)