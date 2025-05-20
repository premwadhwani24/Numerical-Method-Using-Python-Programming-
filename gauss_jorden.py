import numpy as np
def gauss_jordan(a_matrix, b_matrix):
    if a_matrix.shape[0] != a_matrix.shape[1]:
        print("Error: Square Matrix not given!")
        return
    if len(b_matrix.shape) != 2 or b_matrix.shape[1] != 1 or b_matrix.shape[0] != a_matrix.shape[0]:
        print("Error: Constant vector incorrectly sized")
        return
    n = len(b_matrix)
    x = np.zeros(n)
    new_line = "\n"
    augmented_matrix = np.hstack((a_matrix.astype(float), b_matrix.astype(float)))
    print(f"The initial augmented matrix is: {new_line}{augmented_matrix}")
    print("Solving using Gauss-Jordan elimination: ")
    for i in range(n):
        if augmented_matrix[i][i] == 0.0:
            print("Division by zero error")
            return
        pivot = augmented_matrix[i][i]
        augmented_matrix[i] = augmented_matrix[i] / pivot
        for j in range(n):
            if i != j:
                scaling_factor = augmented_matrix[j][i]
                augmented_matrix[j] = augmented_matrix[j] - scaling_factor * augmented_matrix[i]
        print(f"After step {i+1}:\n{augmented_matrix}\n")
    x = augmented_matrix[:, -1]
    print("The solution vector is:")
    for i in range(n):
        print(f"x{i} = {x[i]:.4f}")
variable_matrix = np.array([[1, 2, 3], [2, 8, 22], [3, 22, 82]])
constant_matrix = np.array([[5], [6], [-10]])
gauss_jordan(variable_matrix, constant_matrix)
