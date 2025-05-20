import numpy as np

# Newton's Forward Interpolation Formula:
# f(x) = y0 + pΔy0 + (p(p-1)/2!) Δ^2y0 + (p(p-1)(p-2)/3!) Δ^3y0 + ...
# where p = (x - x0) / h

def newton_forward_interpolation(x, y, value):
    n = len(y)
    diff_table = np.zeros((n, n))
    diff_table[:, 0] = y
    
    for j in range(1, n):
        for i in range(n - j):
            diff_table[i][j] = diff_table[i + 1][j - 1] - diff_table[i][j - 1]
    
    h = x[1] - x[0]
    p = (value - x[0]) / h
    
    interpolation = y[0]
    p_term = 1
    factorial = 1
    
    for i in range(1, n):
        p_term *= (p - (i - 1))
        factorial *= i
        interpolation += (p_term * diff_table[0][i]) / factorial
    
    return interpolation

# Example usage
x = np.array([1,1.4,1.8,2.2], dtype=float)
y = np.array([3.49,4.82,5.96,6.5], dtype=float)  # Example function values
value = 1.6

result = newton_forward_interpolation(x, y, value)
print(f"Interpolated value at x = {value} is {result:.4f}")
