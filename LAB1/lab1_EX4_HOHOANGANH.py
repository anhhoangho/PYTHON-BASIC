# Hồ Hoàng ANh _ 22115054122103

# Exercise4
pay = float(input('amount to pay: '))
paid = float(input('amount paid: '))
yourchange = paid - pay

print('Your change ', round(yourchange,2))
pay = pay * 100
paid = paid * 100

c = paid - pay

dollars = print('Dollars: ', int(c//100))
c = c % 100

quarters = print('Quarters: ', int(c//25))
c = c % 25

dimes = print('Dimes: ', int(c//10))
c = c % 10

nickles = print('Nickles', int(c//5))
c = c % 5

cents = print("Cents: ", int(c))