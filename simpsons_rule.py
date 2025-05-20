import numpy as np

def simpsons_one_third_rule(x, y):
    n = len(x) - 1
    if n % 2 != 0:
        raise ValueError("Simpson's 1/3 rule requires an even number of intervals.")
    
    h = (x[-1] - x[0]) / n
    area = y[0] + y[-1]
    
    for i in range(1, n, 2):
        area += 4 * y[i]
    for i in range(2, n-1, 2):
        area += 2 * y[i]
    
    area *= h / 3
    return area

# Given data
x = np.array([0, 1/6, 2/6, 3/6, 4/6, 5/6, 1])
y = np.array([1.00000, 0.97297, 0.90000, 0.80000, 0.69231, 0.59016, 0.50000])

# Compute the area
try:
    area = simpsons_one_third_rule(x, y)
    print("Approximated Area using Simpson's 1/3 Rule:", round(area, 5))
except ValueError as e:
    print(e)
