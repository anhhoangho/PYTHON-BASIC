# Hồ Hoàng Anh - 22115054122103
def sum(n):
    return n * (n + 1) // 2

def fact1(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def fact2(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact2(n - 1)

def fib1(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def fib2(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib2(n - 1) + fib2(n - 2)

def fib_list(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

def expo1(n):
    e_approx = 1
    for i in range(1, n + 1):
        e_approx += 1 / fact1(i)
    return e_approx

def expo2(n):
    e_approx = 1
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        e_approx += 1 / fact
    return e_approx

n = int(input('Input n: ',))
print("sum:", sum(n))
print("fact1:", fact1(n))
print("fact2:", fact2(n))
print("fib1:", fib1(n))
print("fib2:", fib2(n))
print("fib_list:", fib_list(n))
print("expo1:", expo1(n))
print("expo2:", expo2(n))
