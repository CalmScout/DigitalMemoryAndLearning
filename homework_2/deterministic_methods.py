"""
Deterministic methods implementation: gradient descent and second order(Newton) algorithms
"""
import numpy as np


def dfdx(func, x0, h=1e-4):
    """
    Computes numerical derivative of one variable function.
    """
    return (func(x0 + h) - func(x0 - h)) / (2.0 * h)


def gradient_descent(func, x_init, learning_rate=1e-3, eps=1e-6, iter_limit=1e5):
    """
    Computes function minimum. Stop condition - absolute value of derivative is less than eps
    or number of iterations exceeded. Vanilla implementation.
    """
    iteration = 0
    x = x_init
    grad = dfdx(func, x)
    while np.abs(grad) > eps and iteration < iter_limit:
        x -= learning_rate * grad
        grad = dfdx(func, x)
        iteration += 1
    print("iterations: ", iteration)
    return x


def newton_method(func, x_init, learning_rate=1e-3, eps=1e-6, iter_limit=1e5):
    """
    Seoond order method implementation.
    """
    iteration = 0
    x = x_init
    def d2fdx2(f, x0, h=1e-4):
        """
        Computes second numerical derivative of n in point x0
        """
        return (f(x0 + h) - 2.0*f(x0) + f(x0 - h))/(h * h)
    # magic numbers - initialization for first pass of while loop
    first_derivative = 10.0
    second_derivative = 1.0
    while np.abs(first_derivative / second_derivative) > eps and iteration < iter_limit:
        first_derivative = dfdx(func, x)
        second_derivative = d2fdx2(func, x)
        x -= learning_rate * first_derivative / second_derivative
        iteration += 1
    print(iteration)
    return x

print(newton_method(lambda x: (x - 5)**2, 0.0))
print(gradient_descent(lambda x: (x - 5)**2, 0.0))