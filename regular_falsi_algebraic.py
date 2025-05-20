def f(x):
    return x**3 - 5*x - 7

a = int(input("First initial Guess = "))
b = int(input("Second initial Guess = "))
n = int(input("Number of iterations = "))

if f(a) * f(b) > 0:
    print("False Method Fails")
else:
    k = 1
    while k <= n:
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        print("Root =", round(c, 3), "at iteration =", k)
        k = k + 1
