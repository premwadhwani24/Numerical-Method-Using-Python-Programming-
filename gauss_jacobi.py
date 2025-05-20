import numpy as np

def gauss_jacobi(A, B, initial_guess=None, tol=1e-6, max_iterations=100):
    n = len(B)
    X = np.zeros(n) if initial_guess is None else np.array(initial_guess, dtype=float)
    X_new = np.zeros(n)

    print(f"Initial guess: {X}\n")

    for iteration in range(max_iterations):
        for i in range(n):
            sum1 = sum(A[i][j] * X[j] for j in range(n) if j != i)
            X_new[i] = (B[i] - sum1) / A[i][i]

        print(f"Iteration {iteration+1}: {X_new}")

        # Convergence check (stopping criterion)
        if np.allclose(X, X_new, atol=tol):
            print("\nConverged!")
            break

        X = X_new.copy()

    print("\nThe solution vector is:")
    for i in range(n):
        print(f"x{i} = {X[i]:.6f}")

# Example system of equations
A = np.array([[10, 1, 1], 
              [2, 10, 1], 
              [2, 2, 10]])

B = np.array([12, 13, 14])

initial_guess = [0, 0, 0]  # Starting with zero vector
gauss_jacobi(A, B, initial_guess)
