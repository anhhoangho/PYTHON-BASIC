# Hồ Hoàng anh - 22115054122103

c = input("Enter your temperature: ")
print(c)

doi = c.split('°')
# print(doi)
trong = []
for i in doi:
    y = str(i)
    trong.append(y)

a = float(trong[0])
b = str(trong[1])

# print(a)
# print(b)

if b == 'C':
    dof = 9 / 5 * a + 32
    print('{0}°{1} = {2}°F'.format(a,b,dof))
elif b == 'F':
    doc = 5/9 * (a - 32)
else:
    print('Unknown Scale')

# f = 9/5 * c + 32
# print('The temperature in Fahrenhetit: ', round(f,1))