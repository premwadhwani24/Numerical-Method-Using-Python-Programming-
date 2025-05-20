import numpy as np

def trapezoidal_rule(x, y):
    n = len(x)
    area = 0
    for i in range(n - 1):
        h = x[i + 1] - x[i]  # Width of the trapezoid
        area += (h / 2) * (y[i] + y[i + 1])  # Trapezoidal formula
    return area

# Given data
x = np.array([0, 1/6, 2/6, 3/6, 4/6, 5/6, 1])
y = np.array([1.00000, 0.97297, 0.90000, 0.80000, 0.69231, 0.59016, 0.50000])

# Compute the area
area = trapezoidal_rule(x, y)
print("Approximated Area using Trapezoidal Rule:", round(area, 5))
