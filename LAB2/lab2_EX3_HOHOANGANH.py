name = input("your name? ")
age = int(input('How old are you? '))

if age < 18:
    print('Sorry', name, 'you must be over 18 to drive a car')
else:
    # while True:
    a = input('have you got your driver licence (answer y or n)')
        # if a == 'n' or a == 'y':
        #     break
    if a == 'y':
        print('Ok', name ,'have a good trip!')
    elif a == 'n':
        print('Sorry',name, 'you must hold a driver licence to drive a car')
    else:
        print('answer y or n')
