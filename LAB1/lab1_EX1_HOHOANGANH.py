# Hồ Hoàng ANh _ 22115054122103

# Exercise1
x = int(input('x? '))
y = int(input('Y? '))
print(x, "+", y, "=", x+y)
print(x, "-", y, "=", x-y)
print(x, "X", y, "=", x*y)
print(x, "/", y, "=", x/y)
print(x, "//", y, "=", x//y)
print(x, "%", y, "=", x%y)

# Exercise2
# c = float(input("temperature in Celsius: "))
# f = 9/5 * c + 32
#
# print('The temperature in Fahrenhetit: ', round(f,1))

# Exercise3
sub = float(input('subtotal: '))
tax = float(input('Tax (like 10 for 10%): '))
tip = float(input('Tip (like 10 for 10%): '))

ftax = sub * 15 / 100
ftip = sub * 10 / 100
total = sub + ftax + ftip
print('subtotal: ', sub)
print('Tax (15.0%): ', round(ftax,2))
print('Tip (10.0%): ', ftip)
print('Total: ', round(total,2))



