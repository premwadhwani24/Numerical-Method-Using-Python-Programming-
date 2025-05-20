import numpy as np

# Newton's Backward Interpolation Formula:
#               ∇y_n      ∇^2y_n        ∇^3y_n
# f(x) = y_n + p------ + p(p+1)------ + p(p+1)(p+2)------ + ...
#                1!         2!               3!
# where p = (x - x_n) / h

def newton_backward_interpolation(x, y, value):
    n = len(y)
    diff_table = np.zeros((n, n))
    diff_table[:, 0] = y
    
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            diff_table[i][j] = diff_table[i][j - 1] - diff_table[i - 1][j - 1]
    
    h = x[1] - x[0]
    p = (value - x[-1]) / h
    
    interpolation = y[-1]
    p_term = 1
    factorial = 1
    
    for i in range(1, n):
        p_term *= (p + (i - 1))
        factorial *= i
        interpolation += (p_term * diff_table[-1][i]) / factorial
    
    return interpolation

# Example usage
x = np.array([1931,1941,1951,1961,1971,1981], dtype=float)
y = np.array([12,15,20,27,39,52], dtype=float)  # Example function values
value = 1966

result = newton_backward_interpolation(x, y, value)
print(f"Interpolated value at x = {value} is {result:.4f}")
