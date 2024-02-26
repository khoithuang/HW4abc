# I get help from ChapGPT on how to solve the equations using numpy and scipy and plot the point where the two equations intersect
import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt


def equation1(x):
    """
    Defines the first equation to find its root.

    Parameters:
    - x: The variable for the equation.

    Returns:
    The evaluation of the equation x - 3*cos(x).
    """
    return x - 3 * np.cos(x)


def equation2(x):
    """
    Defines the second equation to find its root.

    Parameters:
    - x: The variable for the equation.

    Returns:
    The evaluation of the equation cos(2*x)*x^2.
    """
    return np.cos(2 * x) * x ** 3


# Find the roots of the equations using fsolve with initial guesses.
# fsolve is used to find the roots of a function, which are the values of x for which the function equals zero.
root1 = fsolve(equation1, 1)  # Initial guess for the first root is 1.
root2 = fsolve(equation2, -1)  # Initial guess for the second root is -1.

print("Root of equation 1:", root1)
print("Root of equation 2:", root2)

# Proceed with plotting if roots are found.
if len(root1) > 0 and len(root2) > 0:
    # Generate a range of x values for plotting the functions.
    x_values = np.linspace(-5, 5, 400)  # Creates a linear space between -5 and 5 with 400 points.

    # Plotting the functions on the same graph for visual comparison and intersection identification.
    plt.plot(x_values, equation1(x_values), label='x - 3*cos(x)')  # Plot equation1.
    plt.plot(x_values, equation2(x_values), label='cos(2*x)*x^2')  # Plot equation2.

    # Highlighting the roots/intersection points on the graph.
    plt.plot(root1, equation1(root1), 'ro', label='Root of Eq1')  # Mark root of equation1.
    plt.plot(root2, equation2(root2), 'ro', label='Root of Eq2')  # Mark root of equation2.

    # Setting up the plot with labels, title, and grid.
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Intersection of Functions')
    plt.legend()
    plt.grid(True)
    plt.show()
else:
    print("No intersection found.")
