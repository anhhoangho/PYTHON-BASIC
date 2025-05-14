# Hồ Hoàng ANh _ 22115054122103

# Exercise3
sub = float(input('subtotal: '))
tax = float(input('Tax (like 10 for 10%): '))
tip = float(input('Tip (like 10 for 10%): '))

ftax = sub * 15 / 100
ftip = sub * 10 / 100

total = sub + ftax + ftip
print('subtotal: ', sub)
print('Tax (',tax,')%: ', round(ftax,2))
print('Tip (',tip,')%: ', round(ftip,2))
print('Total: ', round(total,2))