# I get help from ChatGPT on how to solve the matrix problems using numpy and scipy.
import numpy as np
from scipy.linalg import solve


def solve_matrix_equations():
    """
    Solves two linear algebraic equations:
    1. A 3x3 system of equations.
    2. A 4x4 system of equations.

    Uses numpy arrays to define coefficient matrices and right-hand side vectors,
    then employs scipy's solve function to find the solutions.

    Returns:
        solution1 (numpy.ndarray): Solution vector for the first problem.
        solution2 (numpy.ndarray): Solution vector for the second problem.
    """

    # Define the coefficient matrix and right-hand side vector for the first problem
    # This represents the equation: Ax = b, where A is a 3x3 matrix and b is a 3x1 vector.
    A1 = np.array([[3, 1, -1], [1, 4, 1], [2, 1, 2]])
    b1 = np.array([2, 12, 10])

    # Define the coefficient matrix and right-hand side vector for the second problem
    # This represents the equation: Ax = b, where A is a 4x4 matrix and b is a 4x1 vector.
    A2 = np.array([[1, -10, 2, 4], [3, 1, 4, 12], [9, 2, 3, 4], [-1, 2, 7, 3]])
    b2 = np.array([2, 12, 21, 37])

    # Solve the first system of equations.
    # The solve function finds the vector x that satisfies Ax = b for the given A and b.
    solution1 = solve(A1, b1)

    # Solve the second system of equations.
    solution2 = solve(A2, b2)

    # Return the solutions for both problems.
    return solution1, solution2


# Call the function and print the solutions for both sets of equations
solution1, solution2 = solve_matrix_equations()
print("Solution for the first set of equations:", solution1)
print("Solution for the second set of equations:", solution2)
