import math
def f(x):
    return x * math.log(x) - 1.2  
a = float(input("First initial guess = "))
b = float(input("Second initial guess = "))
if f(a) * f(b) > 0:
    print("Bisection method fails")
else:
    err = float('inf')
    while err > 0.001:
        c = (a + b) / 2
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        err = abs(a - b)
        print("Root =", c)
