height = float(input('enter your height (in meters):'))
weight = float(input('enter your weight (in kilograms):'))

BMI = round(weight / height**2, 1)
print('your BMI is ', BMI)

if BMI <= 15:
    print('your category is very severely underweight')
elif BMI <=16:
    print('your category is severely underweight')
elif BMI <=18.5:
    print('your category is underweight')
elif BMI <=25:
    print('your category is normal')
elif BMI <=30:
    print('your category is overweight')
elif BMI <=35:
    print('your category is moderately obese')
elif BMI <=40:
    print('your category is severely obese')
else:
    print('your category is very severely obese')
