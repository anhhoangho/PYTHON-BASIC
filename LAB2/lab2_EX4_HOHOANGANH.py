import math
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
delta = b**2 - 4 * a * c

if delta < 0:
    print("no real solution")
elif delta == 0:
   print('double solution x1 = x2 =', -(b / (2*a)))
else:
   print('two solution: ',end =' ')
   print('x1 =', (-(b) + math.sqrt(delta))/(2*a),end =',')
   print('x2 =', (-(b) - math.sqrt(delta))/(2*a))

# end là ký tự dòng mới