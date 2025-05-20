def f(X):
    return X**2 - 2*X - 5

def bisection(a, b, n):
    i = 1
    condition = True 
    while condition:
        X = (a + b) / 2
        if f(X) < 0:
            a = X
        else:
            b = X
        # Print results rounded to 3 decimal places
        print(f"Iteration = {i}, X = {X:.3f}, f(X) = {f(X):.3f}")
        if i == n:
            condition = False
        else:
            i += 1
    # Print the final root rounded to 3 decimal places
    print(f"Required root is: {X:.3f}")

# Input values
a = float(input("First approximation root: "))
b = float(input("Second approximation root: "))
n = int(input("No. of Iterations: "))

# Check if the given interval brackets the root
if f(a) * f(b) > 0:
    print("Given approximate roots do not bracket the root.")
    print("Try again with different values.")
else:
    bisection(a, b, n)
