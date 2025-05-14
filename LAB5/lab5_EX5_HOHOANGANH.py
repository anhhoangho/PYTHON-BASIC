# Hồ Hoàng anh - 22115054122103

city = input('Enter the city file path: ')
tem = input('Enter the  temperature file path: ')
out = input('Enter the output file path: ')

# mở file mới để ghi vào
c = open(out, 'w')
with open(city, 'r') as f:
    with open(tem, 'r') as g:
        while True:
            city = f.readline()
            if not city:
                break
            c.write(city.strip() + ' ')
            c.write(g.readline())

c.close()