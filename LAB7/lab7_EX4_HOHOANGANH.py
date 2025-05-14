from random import randint

print('Welcome to the Guessing Game')
print('I\'m thinking of a number between 1 and 100, try to guess it!')

x = randint(0,999)
print('x: ', x)
def guess(n):
    while True:
    # n = int(input('Your Guess: '))
        if n > x:
            print('Too High')
        if n < x:
            print('Too Low')
        if n == x:
            print("Congratulation")
    return x

n = int(input('Your Guess: '))
guess(n)