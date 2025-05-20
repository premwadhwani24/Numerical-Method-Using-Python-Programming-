from sympy import Symbol, lambdify
x = Symbol('x')
f = x**2 - 5*x + 2 
f_prime = f.diff(x) 
f = lambdify(x, f)
f_prime = lambdify(x, f_prime)
x = float(input('Enter the initial guess for x (between 4 and 5): '))
n = int(input("Enter the required correct decimal places: "))
if not (4 <= x <= 5):
    print("Error: Initial guess must be between 0 and 1.")
    exit()
for i in range(1, 4):  
    x_n = x - (f(x) / f_prime(x))  
    print(f"Iteration {i}: x = {x:.{n+2}f}, f(x) = {f(x):.{n+2}f}")
    if round(x_n, n) == round(x, n):
        break
    x = x_n
print(f"Required root (after 3 iterations) is {x:.{n}f}")
