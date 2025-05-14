# Hồ Hoàng anh - 22115054122103
a = input('Input filepath: ')
b = input('Output filepath: ')

# mở file mới để ghi vào
c = open(b, 'w')
with open(a, 'r') as f:
    while True:
        name = f.readline()
        if not name:
            break
        c.write('name: '+ name)
        c.write('Nick name: '+ f.readline())
        c.write('Actor: '+ f.readline()+ '\n')
c.close()