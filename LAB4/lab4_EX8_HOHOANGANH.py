even = []
odd = []

number = input('Your numbers: ')
numbers = number.split(' ')
# print(numbers)
for i in numbers:
    num = int(i)
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print(odd)
print(even)